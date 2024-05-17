from my_parser import parser\

input = "(60 +3)/  ((3+2)*5-18)"

ast_tuple = parser.parse(input)
print(ast_tuple)











