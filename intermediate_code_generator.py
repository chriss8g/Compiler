from TAC import TACOperation, TACFunctionCall, TACConcat, TACPrint
from my_types import STRING_TYPE

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
            self.tac_code.append(TACOperation(node.leaf, arg1, arg2, temp_var, node.data_type))
            node.tac_var = temp_var
            return temp_var

        elif node.type == 'func':
            if node.leaf == 'rand':
                temp_var = self.new_temp()
                self.tac_code.append(TACFunctionCall('rand', [], temp_var))
                return temp_var
            elif node.leaf == 'print':
                arg = self.generate_intermediate_code(node.children[0])
                self.tac_code.append(TACPrint(arg, node.children[0].data_type))
                self.tac_code.append(TACPrint('\n', STRING_TYPE))
                return None
            else:
                args = [self.generate_intermediate_code(child) for child in node.children]
                temp_var = self.new_temp()
                self.tac_code.append(TACFunctionCall(node.leaf, args, temp_var))
                return temp_var

        elif node.type == 'concat':
            arg1 = self.generate_intermediate_code(node.children[0])
            arg2 = self.generate_intermediate_code(node.children[1])
            temp_var = self.new_temp()
            self.tac_code.append(TACConcat(arg1, arg2, temp_var))
            return temp_var
