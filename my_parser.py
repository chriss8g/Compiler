import ply.yacc as yacc
from my_lexer import tokens
from my_ast import ASTNode

# Precedencia de operaciones
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('left', 'GT', 'LT', 'GE', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'POW'),
)

# Definir la regla de producción para los bloques de expresiones
def p_expression_block(p):
    '''expression : LBRACE statements RBRACE'''
    p[0] = ASTNode(type='block', children=p[2])

def p_expression_function(p):
    '''factor : ID LPAREN parameters RPAREN'''
    p[0] = ASTNode(type='function', leaf=p[1], children=p[3])

# Definir la regla de producción para las funciones en línea
def p_function_inline(p):
    '''function : FUNCTION ID LPAREN parameters RPAREN ARROW expression SEMICOLON
                | FUNCTION ID LPAREN RPAREN ARROW expression SEMICOLON'''
    if len(p) == 9:
        p[0] = ASTNode(type='functionDef', leaf=p[2], children=[p[4], p[7]])
    elif len(p) == 8:
        p[0] = ASTNode(type='functionDef', leaf=p[2], children=[[], p[6]])


def p_parameters(p):
    '''parameters : parameters COMA ID
                  | ID
                  | empty'''
    if len(p) == 4:
        p[0] = p[1] + [ASTNode(type='id', leaf=p[3])]
    elif len(p) == 2:
        p[0] = [ASTNode(type='id', leaf=p[1])]
    else:
        p[0] = []

def p_parameters_expression(p):
    '''parameters : expression'''
    p[0] = [p[1]]

def p_empty(p):
    'empty :'
    p[0] = []

# Modificar la regla de statements para incluir funciones
def p_statements(p):
    '''statements : statements statement
                  | statements function
                  | statement
                  | function'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = p[1]

def p_statement(p):
    '''statement : expression SEMICOLON'''
    p[0] = p[1]

# Expresiones
def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:
        p[0] = ASTNode(type='binop', children=[p[1], p[3]], leaf=p[2])
    else:
        p[0] = p[1]

# Términos
def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | term POW factor
            | factor'''
    if len(p) == 4:
        p[0] = ASTNode(type='binop', children=[p[1], p[3]], leaf=p[2])
    else:
        p[0] = p[1]

# Factores
def p_factor_group(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_factor_num_const(p):
    '''factor : NUMBER
              | PI
              | E
              | BOOL
              | STRING
              | ID'''
    if p.slice[1].type == 'NUMBER':
        p[0] = ASTNode(type='num', leaf=p[1])
    elif p.slice[1].type in ('PI', 'E'):
        p[0] = ASTNode(type='const', leaf=p[1])
    elif p.slice[1].type == 'BOOL':
        p[0] = ASTNode(type='bool', leaf=p[1])
    elif p.slice[1].type == 'STRING':
        p[0] = ASTNode(type='string', leaf=p[1])
    elif p.slice[1].type == 'ID':
        p[0] = ASTNode(type='id', leaf=p[1])

def p_factor_func(p):
    '''factor : SIN LPAREN expression RPAREN
              | COS LPAREN expression RPAREN
              | SQRT LPAREN expression RPAREN
              | EXP LPAREN expression RPAREN
              | LOG LPAREN expression COMA expression RPAREN
              | RAND LPAREN RPAREN
              | PRINT LPAREN expression RPAREN'''
    if len(p) == 5:
        p[0] = ASTNode(type='func', children=[p[3]], leaf=p[1])
    elif len(p) == 7:
        p[0] = ASTNode(type='func', children=[p[3], p[5]], leaf=p[1])
    else:
        p[0] = ASTNode(type='func', leaf=p[1])

def p_factor_binop(p):
    '''factor : factor EQ factor
              | factor GT factor
              | factor LT factor
              | factor GE factor
              | factor LE factor
              | factor NE factor'''
    p[0] = ASTNode(type='binco', children=[p[1], p[3]], leaf=p[2])

def p_factor_logicop(p):
    '''factor : factor AND factor
              | factor OR factor'''
    p[0] = ASTNode(type='binlo', children=[p[1], p[3]], leaf=p[2])

def p_factor_concat(p):
    '''factor : factor CONCAT factor'''
    p[0] = ASTNode(type='concat', children=[p[1], p[3]])

def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}' en la línea {p.lineno}, columna {p.lexpos}")
    else:
        print("Error de sintaxis en EOF")
    raise SystemExit("Deteniendo la ejecución debido a un error de sintaxis.")

# Construir el parser
parser = yacc.yacc(start='statements')

if __name__ == "__main__":
    test_data = [
        'function tan(x) => sin(x)/cos(x);',
        'function cot(x) => 1 / tan(x);',
        'print(tan(PI) * tan(PI) + cot(PI) * cot(PI));',
    ]

    for data in test_data:
        print(f"\nAnalizando: {data}")
        try:
            result = parser.parse(data)
            print(result)
        except SystemExit:
            pass
