from my_parser import parser
from semantic_checker import Semantic, SemanticError

class CCodeGenerator:
    def __init__(self, lines):
        self.functions = {}
        self.temp_count = 0
        self.headers = []
        self.body = "int main() {\n"
        self.code = ""
        semantic = Semantic()

        try:
            for line_number, line in enumerate(lines, start=1):

                if not line.strip():
                    continue
                result = parser.parse(line.strip())
                if result:
                    try:
                        semantic.check_semantics(result)
                        c_code = self.generate_c_code(result)
                        self.body += "    " + c_code + ';\n'
                    except SemanticError as e:
                        print(f"Semantic error in line {line_number}: {e}")
                        break

        except Exception as e:
            print(f"Compilation error: {e}")
        
        self.body += "    return 0;\n}\n"

        for i in self.headers:
            self.code += i

        self.code += self.body

    def generate_c_code(self, node):
        if node.type in ('num', 'bool', 'string', 'id'):
            if node.type == 'bool':
                return '1' if node.leaf == 'true' else '0'
            elif node.type == 'string':
                return f'"{node.leaf}"'
            return node.leaf
        
        elif node.type == 'functionDef':
            func_name = node.leaf
            params_node = node.children[0]
            body_node = node.children[1]
            params_code = ", ".join([f"double {arg.leaf}" for arg in params_node])
            func_code = f"double {func_name}({params_code}) {{\n"
            func_body_code = self.generate_c_code(body_node)
            func_code += f"    return {func_body_code};\n}}\n"
            self.headers.append(func_code)
            return ""
        
        elif node.type == 'function':
            func_name = node.leaf
            params_code = ", ".join(f"{self.generate_c_code(arg)}" for arg in node.children)
            return f"{func_name}({params_code})"

        elif node.type == 'block':
            code_block = ""
            for child in node.children:
                code_block += self.generate_c_code(child) + ";\n"
            return "{\n" + code_block + "}"

        elif node.type in ('binop', 'binlo', 'binco'):
            arg1 = self.generate_c_code(node.children[0])
            arg2 = self.generate_c_code(node.children[1])
            if node.leaf == '^':
                s = "#include <math.h>\n"
                if s not in self.headers:
                    self.headers.append(s)

                return f'pow({arg1}, {arg2})'
            return f"({arg1} {node.leaf} {arg2})"

        elif node.type == 'func':
            if node.leaf == 'rand':

                s = "#include <stdlib.h>\n"
                if s not in self.headers:
                    self.headers.append(s)

                return "(double)rand() / RAND_MAX"
            elif node.leaf == 'print':
                
                s = "#include <stdio.h>\n"
                if s not in self.headers:
                    self.headers.append(s)

                arg = self.generate_c_code(node.children[0])
                if node.children[0].data_type == 'int':
                    return f"printf(\"%d\\n\", {arg});"
                elif node.children[0].data_type == 'float':
                    return f"printf(\"%f\\n\", {arg});"
                elif node.children[0].data_type == 'string':
                    return f"printf(\"%s\\n\", {arg});"
                elif node.children[0].data_type == 'bool':
                    return f"printf(\"%d\\n\", {arg});"
            elif node.leaf in ('sin', 'cos', 'sqrt', 'exp', 'log'):
                
                s = "#include <math.h>\n"
                if s not in self.headers:
                    self.headers.append(s)

                arg = self.generate_c_code(node.children[0])
                if node.leaf == 'log':
                    arg2 = self.generate_c_code(node.children[1])
                    return f"log({arg2}) / log({arg})"
                return f"{node.leaf}({arg})"
            else:
                args = ", ".join(self.generate_c_code(child) for child in node.children)
                return f"{node.leaf}({args})"

        elif node.type == 'concat':
            
            s = "#include <string.h>\n"
            if s not in self.headers:
                self.headers.append(s)

            arg1 = self.generate_c_code(node.children[0])
            arg2 = self.generate_c_code(node.children[1])

            arg1 = f'"{arg1}"' if isinstance(arg1, int) else arg1
            arg2 = f'"{arg2}"' if isinstance(arg2, int) else arg2

            s1 = self.new_temp()
            s2 = self.new_temp()
            self.body += f"    char {s1}[{len(arg1) + len(arg2)}] = {arg1};\n"
            self.body += f"    char {s2}[{len(arg2)}] = {arg2};\n"
            self.body += f"    strcat({s1}, {s2});\n"
            return s1

        elif node.type == 'const':
            if node.leaf == 'PI':
                return '3.141592653589793'
            elif node.leaf == 'E':
                return '2.718281828459045'
        elif node.type == 'id':
            return node.leaf

        # Add more cases as necessary for other node types
        return ""

    def new_temp(self):
        self.temp_count += 1
        return f"temp_{self.temp_count}"
