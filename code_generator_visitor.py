import utils.visitor as visitor
from nodes_types import hulk_types as hulk
from nodes_types import c_type as c
from semantic_checker.scope import Scope
import nodes_types.cil as cil


class CodeGeneratorVisitor(object):

    def __init__(self):
        self.headers = ["#define PI  3.141592", "#define E 2.71828"]
        self.aux = []

    @visitor.on('node')
    def visit(self, node, scope=None):
        pass

    @visitor.when(cil.ProgramNode)
    def visit(self, node, scope):
        scope = Scope() if not scope else scope

        dottypes = "\n".join(self.visit(child, scope.create_child_scope())
                             for child in node.dottypes)
        dotdata = "\n".join(self.visit(t, scope.create_child_scope()) for t in node.dotdata)
        dotcode = "\n".join(self.visit(child, scope.create_child_scope())
                            for child in node.dotcode)

        return f'{"\n".join(self.headers)}\n{"\n".join(self.aux)}\n{dottypes}\n{dotdata}\n{dotcode}'

    @visitor.when(cil.TypeNode)
    def visit(self, node, scope):
        struct_name = node.name
        struct_members = "\n    ".join(
            f'{attr.type} {attr.name};' for attr in node.attributes)

        struct_code = f"""
                        typedef struct {{
                            {struct_members}
                        }} {struct_name};
                        """
        return struct_code

    @visitor.when(cil.AllocateNode)
    def visit(self, node, scope):
        header = "#include <stdlib.h>"
        if header not in self.headers:
            self.headers.append(header)

        object_name = node.dest
        code = f"{object_name} = malloc(sizeof({node.type.name}));\n"
        # code += f"memset({object_name}, 0, sizeof({node.type.name}));"
        return code

    @visitor.when(cil.AssignNode)
    def visit(self, node, scope):
        ans = f'{node.dest} = {node.source};'
        return ans

    @visitor.when(cil.LabelNode)
    def visit(self, node, scope):
        return f'{node.label}:'

    @visitor.when(cil.GotoNode)
    def visit(self, node, scope):
        return f'goto {node.label};'

    @visitor.when(cil.GotoIfNode)
    def visit(self, node, scope):
        return f'if ({node.condition}) \n\tgoto {node.label};\nelse \n\tgoto {node.label_else};\n'

    @visitor.when(cil.OurFunctionNode)
    def visit(self, node, scope):
        if node.name == 'printf':
            header = "#include <stdio.h>"
            if header not in self.headers:
                self.headers.append(header)
            if node.type == c.INT_TYPE:
                return f'{node.dest} = printf("%d\\n", {node.source});\n'
            elif node.type == c.FLOAT_TYPE:
                return f'{node.dest} = printf("%f\\n", {node.source});\n'
            elif node.type == c.STRING_TYPE:
                return f'{node.dest} = printf("%s\\n", {node.source});\n'
            else:
                return f'{node.dest} = printf("%d\\n", {node.source});\n'
        elif node.name in ['cos', 'sin', 'exp', 'sqrt', 'log']:
            header = "#include <math.h>"
            if header not in self.headers:
                self.headers.append(header)
            return f'{node.dest} = {node.name}({node.source});\n'
        elif node.name == 'concat':

            header = "#include <string.h>"
            if header not in self.headers:
                self.headers.append(header)
            header = "#include <stdlib.h>"
            if header not in self.headers:
                self.headers.append(header)

            a = '''
                            char* concatenateStrings(const char* str1, const char* str2) {
                                // Calculamos la longitud total de la cadena resultante
                                size_t length1 = strlen(str1);
                                size_t length2 = strlen(str2);
                                size_t totalLength = length1 + length2 + 1; // +1 para el carácter nulo

                                // Reservamos memoria para la cadena resultante
                                char* result = (char*)malloc(totalLength * sizeof(char));
                                if (result == NULL) {
                                    // Si no se pudo asignar memoria, devolvemos NULL
                                    printf("Error: No se pudo asignar memoria.\\n");
                                    return NULL;
                                }

                                // Copiamos la primera cadena en el resultado
                                strcpy(result, str1);
                                // Concatenamos la segunda cadena al resultado
                                strcat(result, str2);

                                return result;
                            }
                        '''
            if a not in self.aux:
                self.aux.append(a)

            return f'{node.dest} = concatenateStrings((char*){node.source}, (char*){node.op_nd});\n'
            

    @visitor.when(cil.FunctionNode)
    def visit(self, node, scope):
        params = ', '.join(self.visit(param, scope.create_child_scope())
                           for param in node.params)
        
        aux = f"{node.type} {node.name}({params});"
        if aux not in self.aux:
            self.aux.append(aux)

        localvars = "\n".join(self.visit(
            var, scope.create_child_scope()) for var in node.localvars)
        # print(node.instructions)
        instructions = "\n".join(self.visit(
            inst, scope.create_child_scope()) for inst in node.instructions)
        return f'{node.type} {node.name}({params}){{ \n{localvars}\n{instructions}\n}}'

    @visitor.when(cil.ParamNode)
    def visit(self, node, scope):
        return f'{node.type} {node.name}'

    @visitor.when(cil.StaticCallNode)
    def visit(self, node, scope):
        return f'{node.dest} = {node.function}();'

    @visitor.when(cil.ReturnNode)
    def visit(self, node, scope):
        return f'return {node.value if node.value is not None else ""};'

    @visitor.when(cil.LocalNode)
    def visit(self, node, scope):
        return f'{node.type} {node.name};'

    @visitor.when(cil.LogicNode)
    def visit(self, node, scope):
        return f'{node.left} {node.op} {node.right}'

    @visitor.when(cil.LoadNode)
    def visit(self, node, scope):
        ans = f'{node.dest} = {node.msg};'
        return ans
    
    @visitor.when(cil.DataNode)
    def visit(self, node, scope):
        return f'#define {node.name} {node.value}'
    