import ply.lex as lex

# Lista de tokens
tokens = (
    'LPAREN',
    'RPAREN',
    # Operadores aritmeticos
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    # Operadores logicos
    'AND',
    'OR',
    'BOOL',
    # Operadores comparativos
    'EQ',
    'GT',
    'LT',
    'GE',
    'LE',
    'NE',
    'PI',
    'E',
    'SIN',
    'COS',
)

# Expresiones regulares para parentesis
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Expresiones regulares para operadores aritmeticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Expresiones regulares para operadores logicos
t_AND = r'&&'
t_OR = r'\|\|'
t_BOOL = r'(true|false)'

# Expresiones regulares para operadores comparativos
t_EQ = r'=='
t_GT = r'>' 
t_LT = r'<' 
t_GE = r'>='
t_LE = r'=<'
t_NE = r'!='

# Constantes
t_PI = r'PI' 
t_E = r'E' 

# Funciones predefinidas
t_SIN = r'sin'
t_COS = r'cos'



# Regla de expresión regular con acción de código
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Ignorar espacios en blanco
t_ignore = ' \t'

# Regla para manejar el error
def t_error(t):
    print("Carácter ilegal '%s' en la línea %d y columna %d" % (t.value[0], t.lineno, t.lexpos))
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba del lexer
if __name__ == "__main__":
    data = "3 == 3"
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
