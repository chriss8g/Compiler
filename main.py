import argparse

from code_generator_visitor import CodeGeneratorVisitor
from my_parser1 import CodeToAST
from semantic_checker_visitor import SemanticCheckerVisitor

def main(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
    

    codeToAST = CodeToAST(text)
    print('\n',codeToAST)


    semantic_checker = SemanticCheckerVisitor()
    errors = semantic_checker.visit(codeToAST.ast)
    if(len(errors) > 0):
        for i, error in enumerate(errors, 1):
            print(f'{i}.', error)

        return
    
    print("✅ Semantic Checked")

    # c_generator = CodeGeneratorVisitor()
    # output = c_generator.visit(codeToAST.ast)

    # with open('script.c', 'w') as output_file:
    #     output_file.write(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate C code from custom script")
    parser.add_argument('input_file', type=str, help='The input file containing the script')
    args = parser.parse_args()

    main(args.input_file)