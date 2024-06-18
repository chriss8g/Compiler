import ply.yacc as yacc
from my_lexer import tokens
from my_ast import ASTNode

# Tabla de contenidos:
# 1. Precedencia de Operaciones
# 2. Definiciones de Producciones
#    2.1. Bloques de Expresiones
#    2.2. Definición de Funciones
#    2.3. Parámetros de Funciones y Expresiones
#    2.4. Definición de Statements
#    2.5. Expresiones Binarias y Términos
#    2.6. Agrupación de Factores, Constantes y Variables
#    2.7. Funciones Matemáticas y Otras
#    2.8. Operadores de Comparación y Lógicos
#    2.9. Concatenación de Cadenas
# 3. Manejo de Errores
# 4. Construcción del Parser
# 5. Prueba del Parser

# 1. Precedencia de Operaciones
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('left', 'GT', 'LT', 'GE', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'POW'),
    ('left', 'ASIGN', 'ASIGN2')
)

# 2. Definiciones de Producciones

def p_asig(p):
    '''asig : ID ASIGN expression'''
    p[0] = ASTNode(type='variable', leaf=p[1], children=p[3])

def p_asig2(p):
    '''asig2 : ID ASIGN2 expression'''
    p[0] = ASTNode(type='asign2', leaf=p[1], children=p[3])

def p_asign2_statement(p):
    '''statement : asig2 SEMICOLON'''
    p[0] = p[1]

def p_asign2_expression(p):
    '''expression : asig2'''
    p[0] = p[1]

def p_asigs(p):
    '''asigs : asigs COMA asig
            | asig'''
    if len(p) == 4:
        p[0] = ASTNode(type='variables', children=p[1].children + [p[3]])
    else:
        p[0] = ASTNode(type='variables', children=[p[1]])

def p_multivariables(p):
    '''statement : LET asigs IN statement'''
    p[0] = ASTNode(type='corpus', children=[p[2], p[4]])

def p_multivariables_expression(p):
    '''expression : LET asigs IN expression'''
    p[0] = ASTNode(type='corpus', children=[p[2], p[4]])

# 2.1. Bloques de Expresiones
def p_expression_block(p):
    '''statement : LBRACE statements RBRACE
                | LBRACE statements RBRACE SEMICOLON'''
    p[0] = ASTNode(type='block', children=p[2])

# 2.2. Definición de Funciones
def p_expression_function(p):
    '''function : ID LPAREN parameters RPAREN'''
    p[0] = ASTNode(type='function', leaf=p[1], children=p[3])

def p_function_inline(p):
    '''functionDef : FUNCTION ID LPAREN parameters RPAREN ARROW expression SEMICOLON
                | FUNCTION ID LPAREN RPAREN ARROW expression SEMICOLON'''
    if len(p) == 9:
        p[0] = ASTNode(type='functionDef', leaf=p[2], children=[p[4], p[7]])
    elif len(p) == 8:
        p[0] = ASTNode(type='functionDef', leaf=p[2], children=[[], p[6]])

def p_function_full(p):
    '''functionDef : FUNCTION ID LPAREN parameters RPAREN LBRACE statements RBRACE
                | FUNCTION ID LPAREN RPAREN LBRACE statements RBRACE'''
    if len(p) == 9:
        p[0] = ASTNode(type='functionDef', leaf=p[2], children=[p[4], p[7]])
    elif len(p) == 8:
        p[0] = ASTNode(type='functionDef', leaf=p[2], children=[[], p[6]])

# 2.3. Parámetros de Funciones y Expresiones
def p_parameters(p):
    '''parameters : parameters COMA expression
                  | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
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

# 2.4. Definición de Statements
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_function(p):
    '''expression : function'''
    p[0] = p[1]

def p_statement(p):
    '''statement : expression SEMICOLON
                    | functionDef'''
    p[0] = p[1]

def p_expression(p):
    '''expression : factor'''
    p[0] = p[1]

# 2.5. Expresiones Binarias y Términos
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression'''
    if len(p) == 4:
        p[0] = ASTNode(type='binop', children=[p[1], p[3]], leaf=p[2])
    else:
        p[0] = p[1]

def p_term_binop(p):
    '''expression : expression TIMES expression
            | expression DIVIDE expression
            | expression POW expression'''
    if len(p) == 4:
        p[0] = ASTNode(type='binop', children=[p[1], p[3]], leaf=p[2])
    else:
        p[0] = p[1]

# 2.6. Agrupación de Factores, Constantes y Variables
def p_factor_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_factor_num_const(p):
    '''factor : NUMBER
              | PI
              | E
              | TRUE
              | FALSE
              | STRING
              | ID'''
    if p.slice[1].type == 'NUMBER':
        p[0] = ASTNode(type='num', leaf=p[1])
    elif p.slice[1].type in ('PI', 'E'):
        p[0] = ASTNode(type='const', leaf=p[1])
    elif p.slice[1].type == 'TRUE':
        p[0] = ASTNode(type='bool', leaf=p[1])
    elif p.slice[1].type == 'FALSE':
        p[0] = ASTNode(type='bool', leaf=p[1])
    elif p.slice[1].type == 'STRING':
        p[0] = ASTNode(type='string', leaf=p[1])
    elif p.slice[1].type == 'ID':
        p[0] = ASTNode(type='id', leaf=p[1])

# 2.7. Funciones Matemáticas y Otras
def p_factor_func(p):
    '''expression : SIN LPAREN expression RPAREN
              | COS LPAREN expression RPAREN
              | SQRT LPAREN expression RPAREN
              | EXP LPAREN expression RPAREN
              | LOG LPAREN expression COMA expression RPAREN
              | RAND LPAREN RPAREN
              | PRINT LPAREN expression RPAREN'''
    if len(p) == 5:
        p[0] = ASTNode(type='func', children=p[3], leaf=p[1])
    elif len(p) == 7:
        p[0] = ASTNode(type='func', children=[p[3], p[5]], leaf=p[1])
    else:
        p[0] = ASTNode(type='func', leaf=p[1])

# 2.8. Operadores de Comparación y Lógicos
def p_factor_binop(p):
    '''expression : expression EQ expression
              | expression GT expression
              | expression LT expression
              | expression GE expression
              | expression LE expression
              | expression NE expression'''
    p[0] = ASTNode(type='binco', children=[p[1], p[3]], leaf=p[2])

def p_factor_logicop(p):
    '''expression : expression AND expression
              | expression OR expression'''
    p[0] = ASTNode(type='binlo', children=[p[1], p[3]], leaf=p[2])

# 2.9. Concatenación de Cadenas
def p_factor_concat(p):
    '''expression : expression CONCAT expression'''
    p[0] = ASTNode(type='concat', children=[p[1], p[3]])

# 3. Manejo de Errores
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p}'")
    else:
        print("Error de sintaxis en EOF")
    raise SystemExit("Deteniendo la ejecución debido a un error de sintaxis.")

# 4. Construcción del Parser
parser = yacc.yacc(start='statement')

# 5. Prueba del Parser
if __name__ == "__main__":
    test_data = [
        'let a = 0 in let b = a := 1 in {print(a);print(b);};'
    ]

    for data in test_data:
        print(f"\nAnalizando: {data}")
        try:
            result = parser.parse(data)
            print(result)
        except SystemExit:
            pass
