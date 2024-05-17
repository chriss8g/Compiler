from my_parser import parser
from semantic_checker import check_semantics, SemanticError
from code_generator import generate_intermediate_code, tac_code

if __name__ == "__main__":
    for i in range(1):
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
            except SemanticError as e:
                print(f"Semantic error: {e}")
