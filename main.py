from my_parser import parser
from semantic_checker import check_semantics, SemanticError
from intermediate_code_generator import IntermediateCodeGenerator
from mips_code_generator import MipsCodeGenerator

if __name__ == "__main__":

    intermediateGenerator = IntermediateCodeGenerator()
    mipsGenerator = MipsCodeGenerator()

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
                        intermediateGenerator.generate_intermediate_code(result)
                    except SemanticError as e:
                        print(f"Semantic error in line {line_number}: {e}")
                        output_file.close()
                        import os
                        os.remove('script.asm')
                        break
            
            mips_code = mipsGenerator.generate_mips_code(intermediateGenerator.tac_code)
            for asm_line in mips_code:
                output_file.write(asm_line + '\n')
            intermediateGenerator.tac_code = []
            intermediateGenerator.temp_count = 0

    except Exception as e:
        print(f"Compilation error: {e}")