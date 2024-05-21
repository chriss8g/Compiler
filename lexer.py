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
    'CONCAT',
    'STRING',
)

# Expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CONCAT = r'@'

# Definición de un número (secuencia de dígitos)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Definicion de una cadena
def t_STRING(t):
    r'"[^"]*"'  # Expresión regular que coincide con una secuencia de caracteres entre comillas dobles.
    t.value = t.value[1:-1]  # ???Elimina las comillas dobles del inicio y final de la cadena.
    # print(t)
    return t  # Devuelve el token procesado.

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
    #data = "3 + 5 * ( 10 - 20 ) / 2"
    data = "\"unstrin\" @ \"otrostrin\""
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
