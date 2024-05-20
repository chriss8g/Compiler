import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'AND',
    'OR', 
    'NOT', 
    'BOOL',
    'LT',  # Menor que
    'GT',  # Mayor que
    'LE',  # Menor o igual
    'GE',  # Mayor o igual
    'EQ',  # Igual
    'NEQ',  # No igual
)

# Expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_AND = r'\bAND\b'
t_OR = r'\bOR\b'
t_NOT = r'\bNOT\b'
t_BOOL = r'(?:\bTRUE\b)|(?:\bFALSE\b)'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NEQ = r'!='

# Definición de un número (secuencia de dígitos)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios en blanco
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba del lexer
if __name__ == "__main__":
    data = "(4+  3 ) >= 4"
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
