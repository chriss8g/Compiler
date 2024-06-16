import ply.lex as lex

# Definir las palabras clave
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
}

# Lista de tokens
tokens = [
    # Caracteres especiales
    'COMA',
    'LPAREN',
    'RPAREN',
    # Operadores aritméticos
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POW',
    # Operadores lógicos
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
    # Strings
    'CONCAT',
    'STRING',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'ARROW',
    'ID',
] + list(keywords.values())

# Definición del token para identificadores (ID)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')  # Verificar si es una palabra clave
    return t

t_ARROW = r'=>'

t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Expresiones regulares para los caracteres especiales
t_COMA = r','
t_SEMICOLON = r';'

# Expresiones regulares para paréntesis
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Expresiones regulares para operadores aritméticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POW = r'\^'

# Expresiones regulares para operadores lógicos
t_AND = r'&&'
t_OR = r'\|\|'

# Expresiones regulares para operadores comparativos
t_EQ = r'=='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_NE = r'!='
t_BOOL = r'\b(true|false)\b'

# Strings
t_CONCAT = r'@'

# Definición de una cadena
def t_STRING(t):
    r'"[^"]*"'  # Expresión regular que coincide con una secuencia de caracteres entre comillas dobles.
    t.value = t.value[1:-1]  # Elimina las comillas dobles del inicio y final de la cadena.
    return t  # Devuelve el token procesado.

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
    # Datos de prueba para varios casos de uso
    test_data = [
        'function sen(x) => sin(x);',
        'function cot(x) => 1 / tan(x);',
        '{ print(tan(PI) * tan(PI) + cot(PI) * cot(PI)); }',
        # # Otros casos de prueba...
    ]

    for data in test_data:
        print(f"\nAnalizando: {data}")
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
