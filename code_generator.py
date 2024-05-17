class TACInstruction:
    def __init__(self, operation, arg1, arg2, result):
        self.operation = operation
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        return f"{self.result} = {self.arg1} {self.operation} {self.arg2}"

tac_code = []
temp_count = 0

def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"

def generate_intermediate_code(node):
    if node.type == 'num':
        return node.leaf

    elif node.type == 'binop':
        arg1 = generate_intermediate_code(node.children[0])
        arg2 = generate_intermediate_code(node.children[1])
        temp_var = new_temp()
        tac_code.append(TACInstruction(node.leaf, arg1, arg2, temp_var))
        return temp_var

if __name__ == "__main__":
    from my_parser import parser
    from semantic_checker import check_semantics, SemanticError

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
                generate_intermediate_code(result)
                print("TAC:")
                for instr in tac_code:
                    print(instr)
                tac_code = []
                temp_count = 0
            except SemanticError as e:
                print(f"Semantic error: {e}")
