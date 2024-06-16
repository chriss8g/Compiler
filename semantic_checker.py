from my_ast import ASTNode

from my_types import NUMBER_TYPE, CONST_TYPE, INT_TYPE, FLOAT_TYPE, STRING_TYPE, BOOL_TYPE


class SemanticError(Exception):
    pass

class Semantic:
    def __init__(self):
        self.functions = {}

    def check_semantics(self, node, expected_type=None):
        if node.type == 'binop':
            left_type = self.check_semantics(node.children[0])
            right_type = self.check_semantics(node.children[1])
            if left_type not in NUMBER_TYPE or right_type not in NUMBER_TYPE:
                raise SemanticError(f"Error semántico: la operación {node.leaf} solo puede aplicarse a números")
            node.data_type = FLOAT_TYPE
            if expected_type and node.data_type != expected_type:
                raise SemanticError(f"Error semántico: la operación {node.leaf} devuelve { node.data_type} pero se esperaba {expected_type}")

        elif node.type == 'functionDef':
            func_name = node.leaf
            if func_name in self.functions:
                raise SemanticError(f"Error semántico: la función {func_name} ya está definida")
            self.functions[func_name] = node
            body_node = node.children[1]
            self.check_semantics(body_node)
            node.data_type = body_node.data_type

        elif node.type == 'function':
            func_name = node.leaf
            if func_name not in self.functions:
                raise SemanticError(f"Error semántico: la función {func_name} no está definida")
            node.data_type = self.functions[func_name].data_type

        elif node.type == 'block':
            for child in node.children:
                self.check_semantics(child)

        elif node.type == 'binlo':
            self.check_semantics(node.children[0], BOOL_TYPE)
            self.check_semantics(node.children[1], BOOL_TYPE)
            node.data_type = BOOL_TYPE
            if expected_type and node.data_type != expected_type:
                raise SemanticError(f"Error semántico: la operación {node.leaf} devuelve {node.data_type} pero se esperaba {expected_type}")

        elif node.type == 'binco':
            left_type = self.check_semantics(node.children[0])
            right_type = self.check_semantics(node.children[1])
            if left_type not in NUMBER_TYPE or right_type not in NUMBER_TYPE:
                raise SemanticError(f"Error semántico: la operación {node.leaf} solo puede aplicarse a números")
            node.data_type = BOOL_TYPE
            if expected_type and node.data_type != expected_type:
                raise SemanticError(f"Error semántico: la operación {node.leaf} devuelve {node.data_type} pero se esperaba {expected_type}")

        elif node.type == 'num':
            if '.' in str(node.leaf):
                node.data_type = FLOAT_TYPE
            else:
                node.data_type = INT_TYPE
            if expected_type and node.data_type != expected_type:
                raise SemanticError(f"Error semántico: el valor {node.leaf} es {node.data_type} pero se esperaba {expected_type}")

        elif node.type == 'bool':
            node.data_type = BOOL_TYPE
            if expected_type and node.data_type != expected_type:
                raise SemanticError(f"Error semántico: el valor {node.leaf} es {node.data_type} pero se esperaba {expected_type}")

        elif node.type == 'func':
            if node.leaf in ('sin', 'cos', 'sqrt', 'exp'):
                arg_type = self.check_semantics(node.children[0])
                if arg_type not in NUMBER_TYPE:
                    raise SemanticError(f"Error semántico: el argumento de la función {node.leaf} debe ser numérico")
                node.data_type = FLOAT_TYPE
            elif node.leaf == 'log':
                arg1_type = self.check_semantics(node.children[0])
                arg2_type = self.check_semantics(node.children[1])
                if arg1_type not in NUMBER_TYPE or arg2_type not in NUMBER_TYPE:
                    raise SemanticError(f"Error semántico: los argumentos de la función {node.leaf} deben ser numéricos")
                node.data_type = FLOAT_TYPE
            elif node.leaf == 'rand':
                node.data_type = FLOAT_TYPE
            elif node.leaf == 'print':
                self.check_semantics(node.children[0])
                node.data_type = STRING_TYPE
            if expected_type and node.data_type != expected_type:
                raise SemanticError(f"Error semántico: la función {node.leaf} devuelve {node.data_type} pero se esperaba {expected_type}")

        elif node.type == 'id':
            node.data_type = CONST_TYPE

        elif node.type == 'const':
            if node.leaf in ('PI', 'E'):
                node.data_type = CONST_TYPE
            else:
                raise SemanticError(
                    f"Error semántico: constante desconocida {node.leaf}")
            if expected_type and node.data_type != expected_type:
                raise SemanticError(f"Error semántico: el valor {node.leaf} es {node.data_type} pero se esperaba {expected_type}")

        elif node.type == 'string':
            node.data_type = STRING_TYPE
            if expected_type and node.data_type != expected_type:
                raise SemanticError(f"Error semántico: el valor {node.leaf} es {node.data_type} pero se esperaba {expected_type}")

        elif node.type == 'concat':
            self.check_semantics(node.children[0])
            self.check_semantics(node.children[1])
            node.data_type = STRING_TYPE
            if expected_type and node.data_type != expected_type:
                raise SemanticError(f"Error semántico: la operación {node.leaf} devuelve {node.data_type} pero se esperaba {expected_type}")

        else:
            raise SemanticError(f"Tipo desconocido de nodo: {node.type}")

        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: se esperaba {expected_type} pero se encontró {node.data_type}")

        return node.data_type


if __name__ == "__main__":
    from my_parser import parser

    test_data = [
        'function tan(x) => sin(x)/cos(x);',
        'function cot(x) => 1 / tan(x);',
        'print(tan(PI) * tan(PI) + cot(PI) * cot(PI));',
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
