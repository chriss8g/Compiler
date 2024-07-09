import argparse

from code_generator_visitor import CodeGeneratorVisitor
from my_parser import CodeToAST
from semantic_checker_visitor import SemanticCheckerVisitor
from CIL_generator_visitor import HULKToCILVisitor
import nodes_types.cil as cil
import os
from collector import Collector
from type_builder import TypeBuilder

def main(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
    

    codeToAST = CodeToAST(text)
    
    if not codeToAST.ast:
        print(codeToAST.error_msg)
        return

    with open('script.uh_ast', 'w') as output_file:
        output_file.write(str(codeToAST))


    # semantic_checker = SemanticCheckerVisitor()
    collector = Collector()
    type_builder = TypeBuilder(collector.context)
    errors = []
    # errors = errors + semantic_checker.visit(codeToAST.ast)
    errors = errors + collector.visit(codeToAST.ast)
    errors = errors + type_builder.visit(codeToAST.ast)
    if(len(errors) > 0):
        for i, error in enumerate(errors, 1):
            print(f'{i}.', error)

        return
    
    print("✅ Semantic Checked")

    cil_generator = HULKToCILVisitor([])
    output = cil_generator.visit(codeToAST.ast)

    from utils.my_format_visitor import FormatVisitor
    formatter = FormatVisitor()

    with open('script.cil', 'w') as output_file:
        output_file.write(formatter.visit(output))

    c_generator = CodeGeneratorVisitor()
    output = c_generator.visit(output, None)

    with open('script.c', 'w') as output_file:
        output_file.write(output)

    os.system("gcc script.c -lm -o script.out && ./script.out")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate C code from custom script")
    parser.add_argument('input_file', type=str, help='The input file containing the script')
    args = parser.parse_args()

    main(args.input_file)