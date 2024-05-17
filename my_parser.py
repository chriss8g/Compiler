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