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
        if node.type in ('num', 'bool', 'string', 'const'):
            return node.leaf

        elif node.type in ('binop', 'binlo', 'binco'):
            arg1 = self.generate_intermediate_code(node.children[0])
            arg2 = self.generate_intermediate_code(node.children[1])
            temp_var = self.new_temp()
            self.tac_code.append(TACInstruction(node.leaf, arg1, arg2, temp_var))
            node.tac_var = temp_var
            return temp_var

        elif node.type == 'func':
            if node.leaf == 'rand':
                temp_var = self.new_temp()
                self.tac_code.append(TACInstruction('rand', '', '', temp_var))
                return temp_var
            else:
                arg1 = self.generate_intermediate_code(node.children[0])
                if len(node.children) > 1:
                    arg2 = self.generate_intermediate_code(node.children[1])
                    temp_var = self.new_temp()
                    self.tac_code.append(TACInstruction(node.leaf, arg1, arg2, temp_var))
                else:
                    temp_var = self.new_temp()
                    self.tac_code.append(TACInstruction(node.leaf, arg1, '', temp_var))
                return temp_var

        elif node.type == 'concat':
            arg1 = self.generate_intermediate_code(node.children[0])
            arg2 = self.generate_intermediate_code(node.children[1])
            temp_var = self.new_temp()
            self.tac_code.append(TACInstruction('@', arg1, arg2, temp_var))
            return temp_var

    def generate_mips_code(self):
        mips_code = [
            ".data",
            "PI: .float 3.141592653589793",
            "E: .float 2.718281828459045",
            ".text",
            "main:"
        ]
        temp_map = {}

        for instr in self.tac_code:
            if instr.result not in temp_map:
                temp_map[instr.result] = f"$f{len(temp_map)}"

            result_reg = temp_map[instr.result]

            if instr.arg1 in temp_map:
                arg1_reg = temp_map[instr.arg1]
            else:
                arg1_reg = instr.arg1

            if instr.arg2 in temp_map:
                arg2_reg = temp_map[instr.arg2]
            else:
                arg2_reg = instr.arg2

            if instr.operation == '+':
                mips_code.append(f"    add.s {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '-':
                mips_code.append(f"    sub.s {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '*':
                mips_code.append(f"    mul.s {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '/':
                mips_code.append(f"    div.s {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '&&':
                mips_code.append(f"    and {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '||':
                mips_code.append(f"    or {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '==':
                mips_code.append(f"    seq {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '!=':
                mips_code.append(f"    sne {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '>':
                mips_code.append(f"    sgt {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '<':
                mips_code.append(f"    slt {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '>=':
                mips_code.append(f"    sge {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == '<=':
                mips_code.append(f"    sle {result_reg}, {arg1_reg}, {arg2_reg}")
            elif instr.operation == 'rand':
                mips_code.append(f"    li {result_reg}, 42")  # Placeholder for random function
            elif instr.operation == '@':
                mips_code.append(f"    concat {result_reg}, {arg1_reg}, {arg2_reg}")

        return mips_code