import argparse

from code_generator_visitor import CodeGeneratorVisitor
from my_parser import CodeToAST
from semantic_checker_visitor import SemanticCheckerVisitor
from CIL_generator_visitor import HULKToCILVisitor
from cmp import cil

def main(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
    

    codeToAST = CodeToAST(text)
    # print('\n',codeToAST)


    # semantic_checker = SemanticCheckerVisitor()
    # errors = semantic_checker.visit(codeToAST.ast)
    # if(len(errors) > 0):
    #     for i, error in enumerate(errors, 1):
    #         print(f'{i}.', error)

    #     return
    
    # print("✅ Semantic Checked")

    cil_generator = HULKToCILVisitor([])
    output = cil_generator.visit(codeToAST.ast)

    formatter = cil.get_formatter()

    # c_generator = CodeGeneratorVisitor()
    # output = c_generator.visit(codeToAST.ast)

    with open('script.cil', 'w') as output_file:
        output_file.write(formatter(output))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate C code from custom script")
    parser.add_argument('input_file', type=str, help='The input file containing the script')
    args = parser.parse_args()

    main(args.input_file)