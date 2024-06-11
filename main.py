from my_parser import parser
from semantic_checker import check_semantics, SemanticError
from code_generator import CodeGenerator

if __name__ == "__main__":

    generator = CodeGenerator()

    with open('script.uh', 'r') as file:
        lines = file.readlines()

    try:
        with open('script.asm', 'w') as output_file:
            for line_number, line in enumerate(lines, start=1):
                if not line.strip():
                    continue
                result = parser.parse(line.strip())
                if result:
                    try:
                        check_semantics(result)
                        generator.generate_intermediate_code(result)
                    except SemanticError as e:
                        print(f"Semantic error in line {line_number}: {e}")
                        output_file.close()
                        import os
                        os.remove('script.asm')
                        break
            
            mips_code = generator.generate_mips_code()
            for asm_line in mips_code:
                output_file.write(asm_line + '\n')
            generator.tac_code = []
            generator.temp_count = 0

    except Exception as e:
        print(f"Compilation error: {e}")