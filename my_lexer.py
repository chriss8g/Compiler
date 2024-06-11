import ply.lex as lex

# Lista de tokens
tokens = (
    # Caracteres especiales
    'COMA',
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
    # Constantes
    'PI',
    'E',
    # Funciones
    'SIN',
    'COS',
    'SQRT',
    'EXP',
    'LOG',
    'RAND',
)

# Expresiones regulares para los caracteres especiales
t_COMA = r','

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
t_SQRT = r'sqrt'
t_EXP = r'exp'
t_LOG = r'log'
t_RAND = r'rand'



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
    data = "log(3,4)"
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
=======
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
