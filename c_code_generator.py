from my_ast import ASTNode
from my_parser import parser
from semantic_checker import Semantic, SemanticError

class CCodeGenerator:
    def __init__(self, lines):
        self.functions = []
        self.variables = {}
        self.temp_count = 0
        self.headers = []
        self.body = "int main() {\n"
        self.code = ""
        self.semantic = Semantic()
        self.contex = ""

        self._process_lines(lines)
        self._finalize_code()

    def _process_lines(self, line):
        result = parser.parse(line)
        if result:
            try:
                self.semantic.check_semantics(result)
            except SemanticError as e:
                print(f"Semantic error: {e}")
            c_code = self.generate_c_code(result)
            self.body += f"    {c_code};\n"

    
    def _finalize_code(self):
        self.body += "    return 0;\n}\n"
        self.code = ''.join(self.headers) + self.contex + self.body

    def generate_c_code(self, node):
        """Genera código C a partir de un nodo AST."""
        # print(node)
        # print(self.variables)
        if node.type in ('num', 'bool', 'string'):
            return self._generate_literal_code(node)
        elif node.type == 'functionDef':
            return self._generate_function_def_code(node)
        elif node.type == 'function':
            return self._generate_function_call_code(node)
        elif node.type == 'block':
            return self._generate_block_code(node)
        elif node.type in ('binop', 'binlo', 'binco'):
            return self._generate_binary_op_code(node)
        elif node.type == 'func':
            return self._generate_builtin_func_code(node)
        elif node.type == 'concat':
            return self._generate_concat_code(node)
        elif node.type == 'const':
            return self._generate_const_code(node)
        elif node.type == 'id':
            # if node.leaf in self.variables.keys():
            #     if(self.variables[node.leaf].children.data_type == 'string'):
            #         return '"' + self.variables[node.leaf].children.leaf + '"'
            #     else:
            #         return self.variables[node.leaf].children.leaf
            # else:
                return node.leaf
        elif node.type == 'corpus':
            return self._generate_corpus_code(node)
        elif node.type == 'variables':
            return self._generate_variables_code(node)
        elif node.type == 'variable':
            return self._generate_variable_code(node)
        # elif node.type == 'variableImp':
        #     return self._generate_variableImp_code(node)
            
        return ""

    def _generate_literal_code(self, node):
        if node.type == 'bool':
            return '1' if node.leaf == 'true' else '0'
        elif node.type == 'string':
            return f'"{node.leaf}"'
        return node.leaf

    def _generate_function_def_code(self, node):
        func_name = node.leaf
        params_node = node.children[0]
        body_node = node.children[1]
        params_code = ", ".join([f"double {arg.leaf}" for arg in params_node])
        func_code = f"double {func_name}({params_code}) {{\n"
        func_body_code = ""
        if isinstance(body_node, list):
            for node in body_node:
                func_body_code += '    ' + self.generate_c_code(node) +'\n'
            func_code += f"    {func_body_code};\n}}\n"
        else:
            func_body_code += self.generate_c_code(body_node)
            func_code += f"    return {func_body_code};\n}}\n"
        self.headers.append(func_code)
        return ""

    def _generate_function_call_code(self, node):
        args = [self.generate_c_code(arg) for arg in node.children]
        func_name = node.leaf
        params_code = ", ".join(f'{i}' for i in args)
        return f"{func_name}({params_code})"

    def _generate_block_code(self, node):
        code_block = ""
        for child in node.children:
            code_block += self.generate_c_code(child) + ";\n"
        return "{\n" + code_block + "}"

    def _generate_binary_op_code(self, node):
        arg1 = self.generate_c_code(node.children[0])
        arg2 = self.generate_c_code(node.children[1])
        if node.leaf == '^':
            self._add_header("#include <math.h>\n")
            return f'pow({arg1}, {arg2})'
        return f"({arg1} {node.leaf} {arg2})"

    def _generate_builtin_func_code(self, node):
        if node.leaf == 'rand':
            self._add_header("#include <stdlib.h>\n")
            return "(double)rand() / RAND_MAX"
        elif node.leaf == 'print':
            self._add_header("#include <stdio.h>\n")
            arg = self.generate_c_code(node.children)
            return self._generate_print_code(node, arg)
        elif node.leaf in ('sin', 'cos', 'sqrt', 'exp'):
            self._add_header("#include <math.h>\n")
            arg = self.generate_c_code(node.children)
            return self._generate_math_func_code(node, arg)
        elif node.leaf == 'log':
            self._add_header("#include <math.h>\n")
            arg = self.generate_c_code(node.children[0])
            return self._generate_math_func_code(node, arg)
        args = ", ".join(self.generate_c_code(child) for child in node.children)
        return f"{node.leaf}({args})"

    def _generate_print_code(self, node, arg):
        if node.children.data_type == 'int':
            return f"printf(\"%d\\n\", {arg});"
        elif node.children.data_type == 'float':
            return f"printf(\"%f\\n\", {arg});"
        elif node.children.data_type == 'string':
            return f"printf(\"%s\\n\", {arg});"
        elif node.children.data_type == 'bool':
            return f"printf(\"%d\\n\", {arg});"

    def _generate_math_func_code(self, node, arg):
        if node.leaf == 'log':
            arg2 = self.generate_c_code(node.children[1])
            return f"(log({arg2}) / log({arg}))"
        return f"{node.leaf}({arg})"

    def _generate_concat_code(self, node):
        self._add_header("#include <string.h>\n")
        self._add_header("#include <stdlib.h>\n")
        arg1 = self.generate_c_code(node.children[0])
        arg2 = self.generate_c_code(node.children[1])
        # print(arg1)
        # print(arg2)
        if("intToString" not in self.functions):
            self.contex += "char* intToString(int num) {static char str[50];sprintf(str, \"%d\", num); return str;}"
            self.functions.append("intToString")
        if("concat" not in self.functions):
            self.contex += "char* concat(const char* s1, const char* s2) {char* result = malloc(strlen(s1) + strlen(s2) + 1);strcpy(result, s1);strcat(result, s2);return result;}"
            self.functions.append("concat")

        if node.children[0].data_type == 'int' and node.children[1].data_type == 'int':
            return f'concat(intToString({arg1}),intToString({arg2}))'
        elif not node.children[0].data_type == 'int' and node.children[1].data_type == 'int':
            return f'concat({arg1},intToString({arg2}))'
        elif node.children[0].data_type == 'int' and not node.children[1].data_type == 'int':
            return f'concat(intToString({arg1}),{arg2})'
        elif not node.children[0].data_type == 'int' and not node.children[1].data_type == 'int':
            return f'concat({arg1},{arg2})'
        

    def _generate_const_code(self, node):
        if node.leaf == 'PI':
            return '3.141592653589793'
        elif node.leaf == 'E':
            return '2.718281828459045'
    
    def _generate_corpus_code(self, node):
        code_block = "{\n"
        t = ""

        t += self.generate_c_code(node.children[0])
        t += self.generate_c_code(node.children[1])

        code_block += t + "}\n"
        self.variables = {}
        return code_block
    
    def _generate_variables_code(self, node):
        t = ""
        for nod in node.children:
            t += self.generate_c_code(nod)
        return t
    
    def _generate_variable_code(self, node):
        # print(node.data_type)
        t = ''
        et = node.leaf
        arg = self.generate_c_code(node.children)
        self.variables[et] = node
        if node.children.data_type == 'int':
            t = f"int {et} = {arg};\n"
        elif node.children.data_type == 'float':
            t = f"float {et} = {arg};\n"
        elif node.children.data_type == 'string':
            t = f"char {et}[] = {arg};\n"
        elif node.children.data_type == 'bool':
            t = f"int {et} = {arg};\n"
        return t
        
    # def _generate_variableImp_code(self, node):
    #     temp = ASTNode(type='variable', leaf=node.leaf, children=node.children)
    #     self.contex += self.generate_c_code(temp)
    #     temp2 = ASTNode(type='id', leaf=node.leaf, children=node.children)
    #     return self.generate_c_code(temp2)

    def _add_header(self, header):
        if header not in self.headers:
            self.headers.append(header)

    def new_temp(self):
        self.temp_count += 1
        return f"temp_{self.temp_count}"

# Main entry point for testing
if __name__ == "__main__":
    test_data = [
        'print(42);'
    ]
    c_generator = CCodeGenerator(test_data)
    print(c_generator.code)
