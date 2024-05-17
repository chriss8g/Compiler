INT_TYPE = 'int'

class SemanticError(Exception):
    pass

def check_semantics(node):
    if node.type == 'binop':
        left_type = check_semantics(node.children[0])
        right_type = check_semantics(node.children[1])
        
        if left_type != right_type:
            raise SemanticError(f"Tipo incompatible en operación binaria: {left_type} y {right_type}")
        
        node.data_type = left_type
        return left_type
    
    elif node.type == 'num':
        node.data_type = INT_TYPE
        return INT_TYPE
    
    else:
        raise SemanticError(f"Tipo desconocido de nodo: {node.type}")

if __name__ == "__main__":
    from my_parser import parser

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
            except SemanticError as e:
                print(f"Semantic error: {e}")
