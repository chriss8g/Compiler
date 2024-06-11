from my_parser import parser
from semantic_checker import check_semantics, SemanticError
from code_generator import CodeGenerator

if __name__ == "__main__":
    generator = CodeGenerator()

    with open('script.uh', 'r') as file:
        lines = file.readlines()

    with open('script.asm', 'w') as output_file:
        for line in lines:
            if not line.strip():
                continue
            result = parser.parse(line.strip())
            if result:
                try:
                    check_semantics(result)
                    generator.generate_intermediate_code(result)
                    mips_code = generator.generate_mips_code()
                    for asm_line in mips_code:
                        output_file.write(asm_line + '\n')
                    generator.tac_code = []
                    generator.temp_count = 0
                except SemanticError as e:
                    print(f"Semantic error: {e}")
