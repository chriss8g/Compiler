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
    '''expression : expression SUMA term
                  | expression RESTA term
                  | term'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 2:
        p[0] = p[1]

def p_expressionL(p):
    '''expressionL : expressionL OR termL
                   | termL'''
    if len(p) == 4:
        if p[2] == '||':
            p[0] = ASTNode(type='binlo', children=[p[1], p[3]], leaf=p[2])
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

def p_termL(p):
    '''termL : termL AND factorL
             | factorL '''
    
    if len(p) == 4:
        if p[2] == '&&':
            p[0] = ASTNode(type='binlo', children=[p[1], p[3]], leaf=p[2])
    elif len(p) == 2:
        p[0] = p[1]


def p_factor(p):
    '''factor : NUMERO
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:  # Caso para paréntesis
        p[0] = p[2]
        
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
               | SIN LPAREN expressionA RPAREN
               | COS LPAREN expressionA RPAREN
               | SQRT LPAREN expressionA RPAREN
               | EXP LPAREN expressionA RPAREN
               | LOG LPAREN expressionA COMA expressionA RPAREN
               | RAND LPAREN RPAREN
               | LPAREN expressionA RPAREN'''
    if len(p) == 2:
        p[0] = ASTNode(type='num', leaf=p[1])
    elif len(p) == 4:
        if p[1] == 'rand':
             p[0] = ASTNode(type='func', leaf=p[1])
        else:
            p[0] = p[2]
    elif len(p) == 5:
        if p[1] == 'sin':
             p[0] = ASTNode(type='func', children=[p[3]], leaf=p[1])
        elif p[1] == 'cos':
            p[0] = ASTNode(type='func', children=[p[3]], leaf=p[1])
        elif p[1] == 'sqrt':
            p[0] = ASTNode(type='func', children=[p[3]], leaf=p[1])
        elif p[1] == 'exp':
            p[0] = ASTNode(type='func', children=[p[3]], leaf=p[1])
    elif len(p) == 7:
        if p[1] == 'log':
            p[0] = ASTNode(type='func', children=[p[3],p[5]], leaf=p[1])
        
def p_expression_concat(p):
    'expression : expression CONCAT expression'
    p[0] = ASTNode(type='concat', children=[p[1], p[3]])

def p_expression_string(p):
    'expression : STRING'
    p[0] = ASTNode(type='string', leaf=p[1])


def p_error(p):
    print(f"Error de sintaxis en '{p}'")
    raise SystemExit("Deteniendo la ejecución debido a un error de sintaxis.")
    
def p_expression_concat(p):
    'expression : expression CONCAT expression'
    p[0] = ASTNode(type='concat', children=[p[1], p[3]])

def p_expression_string(p):
    'expression : STRING'
    p[0] = ASTNode(type='string', leaf=p[1])

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


