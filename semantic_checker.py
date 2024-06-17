from my_ast import ASTNode
from my_types import NUMBER_TYPE, CONST_TYPE, INT_TYPE, FLOAT_TYPE, STRING_TYPE, BOOL_TYPE

class SemanticError(Exception):
    """Clase para manejar errores semánticos."""
    pass

class Semantic:
    """Clase para la comprobación semántica de un árbol AST."""
    def __init__(self):
        self.functions = {}

    def check_semantics(self, node, expected_type=None):
        """Chequea la semántica de un nodo AST."""
        if isinstance(node, list):
            for nod in node:
                self.check_semantics_per_case(nod)
        else:
            return self.check_semantics_per_case(node)
    
    def check_semantics_per_case(self, node, expected_type=None):
        if node.type == 'binop':
                self._check_binop(node, expected_type)
        elif node.type == 'functionDef':
            self._check_function_definition(node)
        elif node.type == 'function':
            self._check_function_call(node)
        elif node.type == 'block':
            self._check_block(node)
        elif node.type == 'binlo':
            self._check_binlo(node, expected_type)
        elif node.type == 'binco':
            self._check_binco(node, expected_type)
        elif node.type == 'num':
            self._check_number(node, expected_type)
        elif node.type == 'bool':
            self._check_boolean(node, expected_type)
        elif node.type == 'func':
            self._check_builtin_function(node, expected_type)
        elif node.type == 'id':
            self._check_identifier(node, expected_type)
        elif node.type == 'const':
            self._check_constant(node, expected_type)
        elif node.type == 'string':
            self._check_string(node, expected_type)
        elif node.type == 'concat':
            self._check_concatenation(node, expected_type)
        else:
            raise SemanticError(f"Tipo desconocido de nodo: {node.type}")

        return node.data_type

    def _check_binop(self, node, expected_type):
        left_type = self.check_semantics(node.children[0])
        right_type = self.check_semantics(node.children[1])
        if left_type not in NUMBER_TYPE or right_type not in NUMBER_TYPE:
            raise SemanticError(f"Error semántico: la operación {node.leaf} solo puede aplicarse a números")
        node.data_type = FLOAT_TYPE
        self._check_expected_type(node, expected_type)

    def _check_function_definition(self, node):
        func_name = node.leaf
        if func_name in self.functions:
            raise SemanticError(f"Error semántico: la función {func_name} ya está definida")
        self.functions[func_name] = node
        body_node = node.children[1]
        self.check_semantics(body_node)
        node.data_type = body_node.data_type

    def _check_function_call(self, node):
        func_name = node.leaf
        if func_name not in self.functions:
            raise SemanticError(f"Error semántico: la función {func_name} no está definida")
        node.data_type = self.functions[func_name].data_type

    def _check_block(self, node):
        for child in node.children:
            self.check_semantics(child)

    def _check_binlo(self, node, expected_type):
        self.check_semantics(node.children[0], BOOL_TYPE)
        self.check_semantics(node.children[1], BOOL_TYPE)
        node.data_type = BOOL_TYPE
        self._check_expected_type(node, expected_type)

    def _check_binco(self, node, expected_type):
        left_type = self.check_semantics(node.children[0])
        right_type = self.check_semantics(node.children[1])
        if left_type not in NUMBER_TYPE or right_type not in NUMBER_TYPE:
            raise SemanticError(f"Error semántico: la operación {node.leaf} solo puede aplicarse a números")
        node.data_type = BOOL_TYPE
        self._check_expected_type(node, expected_type)

    def _check_number(self, node, expected_type):
        node.data_type = FLOAT_TYPE if '.' in str(node.leaf) else INT_TYPE
        self._check_expected_type(node, expected_type)

    def _check_boolean(self, node, expected_type):
        node.data_type = BOOL_TYPE
        self._check_expected_type(node, expected_type)

    def _check_builtin_function(self, node, expected_type):
        if node.leaf in ('sin', 'cos', 'sqrt', 'exp'):
            self._check_numeric_argument(node)
            node.data_type = FLOAT_TYPE
        elif node.leaf == 'log':
            self._check_log_arguments(node)
            node.data_type = FLOAT_TYPE
        elif node.leaf == 'rand':
            node.data_type = FLOAT_TYPE
        elif node.leaf == 'print':
            self.check_semantics(node.children)
            node.data_type = STRING_TYPE
        self._check_expected_type(node, expected_type)

    def _check_identifier(self, node, expected_type):
        node.data_type = CONST_TYPE
        self._check_expected_type(node, expected_type)

    def _check_constant(self, node, expected_type):
        if node.leaf in ('PI', 'E'):
            node.data_type = CONST_TYPE
        else:
            raise SemanticError(f"Error semántico: constante desconocida {node.leaf}")
        self._check_expected_type(node, expected_type)

    def _check_string(self, node, expected_type):
        node.data_type = STRING_TYPE
        self._check_expected_type(node, expected_type)

    def _check_concatenation(self, node, expected_type):
        self.check_semantics(node.children[0])
        self.check_semantics(node.children[1])
        node.data_type = STRING_TYPE
        self._check_expected_type(node, expected_type)

    def _check_numeric_argument(self, node):
        arg_type = self.check_semantics(node.children)
        if arg_type not in NUMBER_TYPE:
            raise SemanticError(f"Error semántico: el argumento de la función {node.leaf} debe ser numérico")

    def _check_log_arguments(self, node):
        arg1_type = self.check_semantics(node.children[0])
        arg2_type = self.check_semantics(node.children[1])
        if arg1_type not in NUMBER_TYPE or arg2_type not in NUMBER_TYPE:
            raise SemanticError(f"Error semántico: los argumentos de la función {node.leaf} deben ser numéricos")

    def _check_expected_type(self, node, expected_type):
        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: se esperaba {expected_type} pero se encontró {node.data_type}")

if __name__ == "__main__":
    from my_parser import parser

    test_data = [
        'function tan(x) => sin(x) / cos(x);\nprint(tan(PI));'
    ]
    semantic = Semantic()

    for data in test_data:
        print(f"\nAnalizando: {data}")
        try:
            result = parser.parse(data)
            if result:
                semantic.check_semantics(result)
                print("Semantics check passed")
                print(result)
        except SemanticError as e:
            print(f"Semantic error: {e}")
        except Exception as e:
            print(f"Syntax or other error: {e}")
