import ply.lex as lex

# Definir las palabras clave y sus tokens correspondientes
keywords = {
    'function': 'FUNCTION',
    'sin': 'SIN',
    'cos': 'COS',
    'sqrt': 'SQRT',
    'exp': 'EXP',
    'log': 'LOG',
    'rand': 'RAND',
    'print': 'PRINT',
    'PI': 'PI',
    'E': 'E',
    'let': 'LET',
    'in': 'IN'
}

# Lista de tokens, incluyendo las palabras clave
tokens = [
    'COMA', 'LPAREN', 'RPAREN', 
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POW',
    'AND', 'OR', 'BOOL',
    'EQ', 'GT', 'LT', 'GE', 'LE', 'NE',
    'CONCAT', 'STRING', 'LBRACE', 'RBRACE', 'SEMICOLON', 'ARROW', 'ID', 'ASIGN', 'ASIGN2'
] + list(keywords.values())

# Expresiones regulares para tokens simples
t_COMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POW = r'\^'
t_AND = r'&&'
t_OR = r'\|\|'
t_EQ = r'=='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_NE = r'!='
t_BOOL = r'\b(true|false)\b'
t_CONCAT = r'@'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_ARROW = r'=>'
t_ASIGN = r'='
t_ASIGN2 = r':='


# Definición del token para identificadores (ID) y palabras clave
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')  # Verificar si es una palabra clave
    return t

# Definición de un número (entero o flotante)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Definición de una cadena
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Elimina las comillas dobles del inicio y final de la cadena
    return t

# Caracteres a ignorar (espacios en blanco y tabulaciones)
t_ignore = ' \t\n\r'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno} y columna {t.lexpos}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Prueba del lexer
if __name__ == "__main__":
    test_data = [
        'let a = 6, b = a * 7 in print(b);'
    ]

    for data in test_data:
        print(f"\nAnalizando: {data}")
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
