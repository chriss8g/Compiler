import ply.yacc as yacc
from my_lexer import tokens
from my_ast import ASTNode

# Precedencia de operaciones
precedence = (
    ('left', 'OR'), 
    ('left', 'AND'), 
    ('left', 'EQ', 'GT', 'LT', 'GE', 'LE', 'NE'),
    ('left', 'PLUS', 'MINUS'), 
    ('left', 'TIMES', 'DIVIDE'),
)

def p_expression(p):
    '''expression : expressionL
                  | expressionA'''
    if len(p) == 2:
        p[0] = p[1]

def p_expressionL(p):
    '''expressionL : expressionL OR termL
                   | termL'''
    if len(p) == 4:
        if p[2] == '||':
            p[0] = ASTNode(type='binlo', children=[p[1], p[3]], leaf=p[2])
    elif len(p) == 2:
        p[0] = p[1]

def p_termL(p):
    '''termL : termL AND factorL
             | factorL '''
    
    if len(p) == 4:
        if p[2] == '&&':
            p[0] = ASTNode(type='binlo', children=[p[1], p[3]], leaf=p[2])
    elif len(p) == 2:
        p[0] = p[1]

def p_factorL(p):
    '''factorL : BOOL
               | factorA EQ factorA
               | factorA GT factorA
               | factorA LT factorA
               | factorA GE factorA
               | factorA LE factorA
               | factorA NE factorA
               | LPAREN expressionL RPAREN'''
    if len(p) == 4:
        if p[2] == '==':
            p[0] = ASTNode(type='binco', children=[p[1], p[3]], leaf=p[2])
        elif p[2] == '>':
            p[0] = ASTNode(type='binco', children=[p[1], p[3]], leaf=p[2])
        elif p[2] == '<':
            p[0] = ASTNode(type='binco', children=[p[1], p[3]], leaf=p[2])
        elif p[2] == '>=':
            p[0] = ASTNode(type='binco', children=[p[1], p[3]], leaf=p[2])
        elif p[2] == '=<':
            p[0] = ASTNode(type='binco', children=[p[1], p[3]], leaf=p[2])
        elif p[2] == '!=':
            p[0] = ASTNode(type='binco', children=[p[1], p[3]], leaf=p[2])
        else:  # Caso para paréntesis
            p[0] = p[2]
    if len(p) == 2:
        p[0] = ASTNode(type='bool', leaf=p[1])
    

def p_expressionA(p):
    '''expressionA : expressionA PLUS termA
                   | expressionA MINUS termA
                   | termA'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = ASTNode(type='binop', children=[p[1], p[3]], leaf=p[2])
        if p[2] == '-':
            p[0] = ASTNode(type='binop', children=[p[1], p[3]], leaf=p[2])  
    elif len(p) == 2:
        p[0] = p[1]

def p_termA(p):
    '''termA : termA TIMES factorA
             | termA DIVIDE factorA
             | factorA '''
    
    if len(p) == 4:
        if p[2] == '*':
            p[0] = ASTNode(type='binop', children=[p[1], p[3]], leaf=p[2])
        if p[2] == '/':
            p[0] = ASTNode(type='binop', children=[p[1], p[3]], leaf=p[2])  
    elif len(p) == 2:
        p[0] = p[1]

def p_factorA(p):
    '''factorA : NUMBER
               | PI
               | E
               | SIN LPAREN expression RPAREN
               | COS LPAREN expression RPAREN
               | LPAREN expressionA RPAREN'''
    if len(p) == 2:
        p[0] = ASTNode(type='num', leaf=p[1])
    elif len(p) == 5:
        if p[1] == 'sin':
             p[0] = ASTNode(type='func', children=[p[3]], leaf=p[1])
        elif p[1].lower() == 'cos':
            p[0] = ASTNode(type='func', children=[p[3]], leaf=p[1])
    else:  # Caso para paréntesis
        p[0] = p[2]

def p_error(p):
    print(f"Error de sintaxis en '{p}'")
    raise SystemExit("Deteniendo la ejecución debido a un error de sintaxis.")

parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        result.imprimir()
=======
import ply.yacc as yacc
from my_lexer import tokens
    
# Precedencia de operaciones
precedence = (
    ('left', 'SUMA', 'RESTA'), 
    ('left', 'MULTIPLICACION', 'DIVISION'), 
)

# Reglas de la gramática
def p_expression(p):
    '''expression : expression SUMA term
                  | expression RESTA term
                  | term'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 2:
        p[0] = p[1]

def p_term(p):
    '''term : term MULTIPLICACION factor
            | term DIVISION factor
            | factor '''
    
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 2:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMERO
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:  # Caso para paréntesis
        p[0] = p[2]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Construir el parser
parser = yacc.yacc()
