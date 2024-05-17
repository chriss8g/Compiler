from my_parser import parser
from semantic_checker import check_semantics, SemanticError
from code_generator import code_generator

if __name__ == "__main__":
    while(1):
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
                x = code_generator()
                x.generate_intermediate_code(result)
                print("TAC:")
                for instr in x.tac_code:
                    print(instr)
            except SemanticError as e:
                print(f"Semantic error: {e}")
