from my_parser import parser
from semantic_checker import check_semantics, SemanticError
from code_generator import CodeGenerator

if __name__ == "__main__":
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
