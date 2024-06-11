from my_ast import ASTNode

INT_TYPE = 'int'
BOOL_TYPE = 'bool'

class SemanticError(Exception):
    pass

def check_semantics(node, type=''):
    if node.type == 'binop':
        if type != 'num':
            raise SemanticError(f"Error semántico, la operación {node.leaf} devuelve un num")
        
        check_semantics(node.children[0], type)
        check_semantics(node.children[1], type)

        node.data_type = INT_TYPE

    elif node.type == 'binlo':
        if type != 'bool':
            raise SemanticError(f"Error semántico, la operación {node.leaf} devuelve un bool")
        
        check_semantics(node.children[0], 'bool')
        check_semantics(node.children[1], 'bool')

        node.data_type = BOOL_TYPE
    
    elif node.type == 'binco':
        if type != 'bool':
            raise SemanticError(f"Error semántico, la operación {node.leaf} devuelve un bool")
        
        check_semantics(node.children[0], 'num')
        check_semantics(node.children[1], 'num')

        node.data_type = BOOL_TYPE

    elif node.type == 'num':
        if type != 'num':
            raise SemanticError(f"Error semántico, el valor {node.leaf} es un num")
        
        node.data_type = INT_TYPE
        return INT_TYPE
    
    elif node.type == 'bool':
        if type != 'bool':
            raise SemanticError(f"Error semántico, el valor {node.leaf} es un bool")
        
        node.data_type = BOOL_TYPE
        return BOOL_TYPE
    
    else:
        raise SemanticError(f"Tipo desconocido de nodo: {node.type}")
    
    if type == '':
        node.data_type = node.children[0].data_type

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
                check_semantics(result, 'bool')
                print("Semantics check passed")
            except SemanticError as e:
                print(f"Semantic error: {e}")
