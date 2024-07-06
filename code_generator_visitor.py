import utils.visitor as visitor
from nodes_types import hulk_types as hulk
from semantic_checker.scope import Scope
import nodes_types.cil as cil

class CodeGeneratorVisitor(object):

    def __init__(self):
        self.headers = ["#define PI  3.141592", "#define E 2.71828"]

    @visitor.on('node')
    def visit(self, node, scope=None):
        pass

    @visitor.when(cil.ProgramNode)
    def visit(self, node, scope):

        scope = Scope() if not scope else scope
    
        dottypes = ""
        dottypes = dottypes + '\n    '.join(self.visit(child, scope.create_child_scope()) for child in node.dottypes)

        dotdata = ''
        for t in node.dotdata:
            dotdata = dotdata + '#define' + self.visit(t, scope.create_child_scope()) + "\n"

        dotcode = ""
        dotcode = dotcode + '\n    '.join(self.visit(child, scope.create_child_scope()) for child in node.dotcode)

        return f'{"\n".join(self.headers)}' + f'{dottypes}\n{dotdata}\n{dotcode}'


    @visitor.when(cil.LabelNode)
    def visit(self, node, scope):
        return f'{node.label}:'
    
    @visitor.when(cil.GotoNode)
    def visit(self, node, scope):
        return f'goto {node.label};'
    
    @visitor.when(cil.GotoIfNode)
    def visit(self, node, scope):
        ans = f'if( {node.condition}) \n\tgoto {node.label};\n else \n\tgoto {node.label_else};\n'
        return f'{ans}'
        
    @visitor.when(cil.OurFunctionNode)
    def visit(self, node, scope):

        if node.name == 'printf':
            header = "#include <stdio.h>"
            if(header not in self.headers):
                self.headers.append(header)

            ans = f'{node.dest} = printf("%f\\n", {node.source});\n'
            return f'{ans}'
        elif(node.name == 'cos'):
            header = "#include <math.h>"
            if(header not in self.headers):
                self.headers.append(header)

            ans = f'{node.dest} = cos({node.source});\n'
            return f'{ans}'
        elif(node.name == 'sin'):
            header = "#include <math.h>"
            if(header not in self.headers):
                self.headers.append(header)

            ans = f'{node.dest} = sin({node.source});\n'
            return f'{ans}'
        elif(node.name == 'exp'):
            header = "#include <math.h>"
            if(header not in self.headers):
                self.headers.append(header)

            ans = f'{node.dest} = exp({node.source});\n'
            return f'{ans}'
    
    
    @visitor.when(cil.FunctionNode)
    def visit(self, node, scope):
        params = ', '.join(self.visit(x, scope.create_child_scope()) for x in node.params)

        localvars = ""
        for x in node.localvars:
            localvars = localvars + self.visit(x, scope.create_child_scope()) + ";\n"

        instructions = ""
        for x in node.instructions:
            instructions = instructions + self.visit(x, scope.create_child_scope()) + '\n'

        return f'int {node.name}({params}){{ \n{localvars}\n{instructions} }}'
    
    @visitor.when(cil.ParamNode)
    def visit(self, node, tabs=0):
        return f'int {node.name}'

    @visitor.when(cil.StaticCallNode)
    def visit(self, node, scope):
        return f'{node.dest} = {node.function}();'
    
    @visitor.when(cil.ReturnNode)
    def visit(self, node, scope):
        return f'return {node.value if node.value is not None else ""};'
    
    @visitor.when(cil.LocalNode)
    def visit(self, node, scope):
        return f'float {node.name}'
    
    @visitor.when(cil.LogicNode)
    def visit(self, node, scope):
        ans = f'{node.left} {node.op} {node.right}'
        return f'{ans}'
    
    @visitor.when(cil.AssignNode)
    def visit(self, node, scope):
        ans = f'{node.dest} = {node.source} * 1.0;'
        return ans
    

    @visitor.when(cil.TypeNode)
    def visit(self, node, tabs=0):
        object_name = node.name
        properties = node.attributes

        code = "\n"
        
        # Define indices for each property with specific object prefix
        for i, prop_name in enumerate(properties):
            code += f"#define {object_name.upper()}_{prop_name.dest.upper()} {i}\n"
        code += f"#define {object_name.upper()}_NUM_PROPS {len(properties)}\n\n"

        # Initialize function
        code += f"void inicializar{object_name}(void *{object_name.lower()}"
        code += f") {{\n"

        for prop_name in properties:
            code += f"    int *p{prop_name.dest.capitalize()} = (int *)((char *){object_name.lower()} + {object_name.upper()}_{prop_name.dest.upper()});\n"
            code += f"    *p{prop_name.dest.capitalize()} = {prop_name.source};\n"
        code += f"}}\n\n"

        # Getter functions
        for prop_name in properties:
            code += f"int obtener{prop_name.dest.capitalize()}{object_name}(void *{object_name.lower()}) {{\n"
            code += f"    int *p{prop_name.dest.capitalize()} = (int *)((char *){object_name.lower()} + {object_name.upper()}_{prop_name.dest.upper()});\n"
            code += f"    return *p{prop_name.dest.capitalize()};\n"
            code += f"}}\n\n"

        return code
    
    @visitor.when(cil.AllocateNode)
    def visit(self, node, tabs=0):

        header = "#include <stdlib.h>"
        if(header not in self.headers):
            self.headers.append(header)

        object_name = node.dest
        code = f"\t{object_name.lower()} = malloc({len(node.type.attributes)} * sizeof(int));\n"
        code += f"    inicializar{node.type.name}({object_name.lower()});\n"
        return code


    # # Example usage:
    # object_name1 = "Persona"
    # properties1 = ["nombre", "edad", "altura"]

    # object_name2 = "Vehiculo"
    # properties2 = ["marca", "modelo", "year"]

    # c_code_persona = generate_c_code(object_name1, properties1)
    # c_code_vehiculo = generate_c_code(object_name2, properties2)

    # print("Código para Persona:\n")
    # print(c_code_persona)
    # print("\nCódigo para Vehiculo:\n")
    # print(c_code_vehiculo)
                