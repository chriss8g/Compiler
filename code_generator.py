from my_ast import ASTNode

class TACInstruction:
    def __init__(self, operation, arg1, arg2, result):
        self.operation = operation
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        return f"{self.result} = {self.arg1} {self.operation} {self.arg2}"

class CodeGenerator:
    def __init__(self):
        self.tac_code = []
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate_intermediate_code(self, node):
        if node.type == 'num':
            return node.leaf

        elif node.type == 'binop':
            arg1 = self.generate_intermediate_code(node.children[0])
            arg2 = self.generate_intermediate_code(node.children[1])
            temp_var = self.new_temp()
            self.tac_code.append(TACInstruction(node.leaf, arg1, arg2, temp_var))
            node.tac_var = temp_var
            return temp_var

    def generate_mips_code(self):
        mips_code = []
        for instr in self.tac_code:
            if instr.operation == '+':
                mips_code.append(f"add {instr.result}, {instr.arg1}, {instr.arg2}")
            elif instr.operation == '-':
                mips_code.append(f"sub {instr.result}, {instr.arg1}, {instr.arg2}")
            elif instr.operation == '*':
                mips_code.append(f"mul {instr.result}, {instr.arg1}, {instr.arg2}")
            elif instr.operation == '/':
                mips_code.append(f"div {instr.result}, {instr.arg1}, {instr.arg2}")
        return mips_code

if __name__ == "__main__":
    from my_parser import parser
    from semantic_checker import check_semantics, SemanticError

    generator = CodeGenerator()

    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        if result:
            try:
                check_semantics(result)
                print("Semantics check passed")
                generator.generate_intermediate_code(result)
                print("TAC:")
                for instr in generator.tac_code:
                    print(instr)
                print("MIPS Code:")
                mips_code = generator.generate_mips_code()
                for line in mips_code:
                    print(line)
                generator.tac_code = []
                generator.temp_count = 0
            except SemanticError as e:
                print(f"Semantic error: {e}")
