import argparse
from c_code_generator import CCodeGenerator

def main(input_file):
    with open(input_file, 'r') as file:
        lines = '\n'.join(file.readlines())
    lines = '{' + lines + '}'
    cGenerator = CCodeGenerator(lines)

    with open('script.c', 'w') as output_file:
        output_file.write(cGenerator.code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate C code from custom script")
    parser.add_argument('input_file', type=str, help='The input file containing the script')
    args = parser.parse_args()

    main(args.input_file)
