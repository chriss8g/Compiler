
class TACInstruction:
    def __init__(self, operation, arg1, arg2, result):
        self.operation = operation
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        return f"{self.result} = {self.arg1} {self.operation} {self.arg2}"

class IntermediateCodeGenerator:
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
            elif node.leaf == 'print':
                arg = self.generate_intermediate_code(node.children[0])
                temp_var = self.new_temp()
                self.tac_code.append(TACInstruction('print', arg, '', temp_var))
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
