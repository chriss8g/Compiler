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
    ('left', 'TIMES', 'DIVIDE'),
)

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
              | STRING'''
    if p.slice[1].type == 'NUMBER':
        p[0] = ASTNode(type='num', leaf=p[1])
    elif p.slice[1].type in ('PI', 'E'):
        p[0] = ASTNode(type='const', leaf=p[1])
    elif p.slice[1].type == 'BOOL':
        p[0] = ASTNode(type='bool', leaf=p[1])
    elif p.slice[1].type == 'STRING':
        p[0] = ASTNode(type='string', leaf=p[1])


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
    print(f"Error de sintaxis en '{p}'")
    raise SystemExit("Deteniendo la ejecución debido a un error de sintaxis.")

# Construir el parser
parser = yacc.yacc()

if __name__ == "__main__":
    test_data = [
        'print(5)',
        "PI + E",                       # Constantes
        "sin(PI / 2)",                  # Funciones trigonométricas
        "3 + 4.5 * 10",                 # Operaciones aritméticas con decimales
        "(3 + 4) * 10.5",               # Uso de paréntesis con decimales
        "true && false || true",        # Operadores lógicos
        "3.0 >= 2",                     # Operadores comparativos con decimales
        '"Hello" @ " World!"',          # Concatenación de cadenas
        'log(100, 10)',                 # Función logarítmica
        'rand()',                       # Función random
        "3.14 + 2.71",                  # Números flotantes
        "5 == 5",                       # Comparación de igualdad
        "10 != 20",                     # Comparación de desigualdad
        "sqrt(4)",                      # Función raíz cuadrada
        "exp(1)",                       # Función exponencial
        "4 / 2.0",                      # División con decimales
        "10 - 5",                       # Resta
        "true",                         # Booleano true
        "false",                        # Booleano false
        "sin(PI) + cos(E)",             # Combinación de funciones y constantes
        "3.0 + true",                   # Error: combinación inválida de tipos
        'log("hello", 10)',             # Error: tipo incorrecto en función logarítmica
        'PI + "hello"',                 # Error: combinación inválida de tipos
    ]

    for data in test_data:
        print(f"\nAnalizando: {data}")
        result = parser.parse(data)
        print(result)
