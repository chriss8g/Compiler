import argparse

from code_generator_visitor import CodeGeneratorVisitor
from my_parser import CodeToAST
from CIL_generator_visitor import HULKToCILVisitor
import nodes_types.cil as cil
import os
from collector import Collector
from type_builder import TypeBuilder
from nodes_types import hulk_types as hulk

def main(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
    

    codeToAST = CodeToAST(text)
    
    if not codeToAST.ast:
        print(codeToAST.error_msg)
        return

    with open('script.uh_ast', 'w') as output_file:
        output_file.write(str(codeToAST))


    collector = Collector()
    errors = []
    errors = errors + collector.visit(codeToAST.ast)
    collector.context.create_type(hulk.BOOL_TYPE)
    collector.context.create_type(hulk.NUMBER_TYPE)
    collector.context.create_type(hulk.STRING_TYPE)
    type_builder = TypeBuilder(collector.context)
    errors = errors + type_builder.visit(codeToAST.ast)
    if(len(errors) > 0):
        for i, error in enumerate(errors, 1):
            print(f'{i}.', error)

        return
    
    cil_generator = HULKToCILVisitor({})
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

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Generate C code from custom script")
#     parser.add_argument('input_file', type=str, help='The input file containing the script')
#     args = parser.parse_args()

    # main(args.input_file)
main('./script.uh')
