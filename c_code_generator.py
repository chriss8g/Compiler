from my_parser import parser
from semantic_checker import Semantic, SemanticError

class CCodeGenerator:
    def __init__(self, lines):
        self.functions = {}
        self.temp_count = 0
        self.headers = []
        self.body = "int main() {\n"
        self.code = ""
        self.semantic = Semantic()
        self.dudes = []

        self._process_lines(lines)
        self._finalize_code()

    def _process_lines(self, lines):
        for line_number, line in enumerate(lines, start=1):
            if not line.strip():
                continue
            result = parser.parse(line.strip())
            if result:
                state = self.semantic.functions.copy()
                if not self._check_semantics(result, state):
                    self.dudes.append(result)
                    self.semantic.functions = state
                    continue
                c_code = self.generate_c_code(result)
                self.body += f"    {c_code};\n"
        
        self._process_dudes()

    def _check_semantics(self, result, state):
        try:
            self.semantic.check_semantics(result)
            return True
        except SemanticError:
            return False

    def _process_dudes(self):
        for line in self.dudes:
            try:
                self.semantic.check_semantics(line)
            except SemanticError as e:
                print(f"Semantic error: {e}")
                break
            c_code = self.generate_c_code(line)
            self.body += f"    {c_code};\n"

    def _finalize_code(self):
        self.body += "    return 0;\n}\n"
        self.code = ''.join(self.headers) + self.body

    def generate_c_code(self, node):
        """Genera código C a partir de un nodo AST."""
        if node.type in ('num', 'bool', 'string', 'id'):
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
            return node.leaf
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
        func_body_code = self.generate_c_code(body_node)
        func_code += f"    return {func_body_code};\n}}\n"
        self.headers.append(func_code)
        return ""

    def _generate_function_call_code(self, node):
        func_name = node.leaf
        params_code = ", ".join(self.generate_c_code(arg) for arg in node.children)
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
            arg = self.generate_c_code(node.children[0])
            return self._generate_print_code(node, arg)
        elif node.leaf in ('sin', 'cos', 'sqrt', 'exp', 'log'):
            self._add_header("#include <math.h>\n")
            arg = self.generate_c_code(node.children[0])
            return self._generate_math_func_code(node, arg)
        args = ", ".join(self.generate_c_code(child) for child in node.children)
        return f"{node.leaf}({args})"

    def _generate_print_code(self, node, arg):
        if node.children[0].data_type == 'int':
            return f"printf(\"%d\\n\", {arg});"
        elif node.children[0].data_type == 'float':
            return f"printf(\"%f\\n\", {arg});"
        elif node.children[0].data_type == 'string':
            return f"printf(\"%s\\n\", {arg});"
        elif node.children[0].data_type == 'bool':
            return f"printf(\"%d\\n\", {arg});"

    def _generate_math_func_code(self, node, arg):
        if node.leaf == 'log':
            arg2 = self.generate_c_code(node.children[1])
            return f"(log({arg2}) / log({arg}))"
        return f"{node.leaf}({arg})"

    def _generate_concat_code(self, node):
        self._add_header("#include <string.h>\n")
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

    def _generate_const_code(self, node):
        if node.leaf == 'PI':
            return '3.141592653589793'
        elif node.leaf == 'E':
            return '2.718281828459045'

    def _add_header(self, header):
        if header not in self.headers:
            self.headers.append(header)

    def new_temp(self):
        self.temp_count += 1
        return f"temp_{self.temp_count}"

# Main entry point for testing
if __name__ == "__main__":
    test_data = [
        'function tan(x) => sin(x)/cos(x);',
        'function cot(x) => 1 / tan(x);',
        'print(tan(PI) * tan(PI) + cot(PI) * cot(PI));',
    ]
    c_generator = CCodeGenerator(test_data)
    print(c_generator.code)
