import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'LPAREN',
    'RPAREN',
)

# Reglas de expresiones regulares para tokens simples
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Regla de expresión regular con acción de código
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Ignoring whitespace
t_ignore = ' \t'

# Regla para manejar errores
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

