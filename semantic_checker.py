from my_ast import ASTNode

INT_TYPE = 'int'
FLOAT_TYPE = 'float'
BOOL_TYPE = 'bool'
STRING_TYPE = 'string'

class SemanticError(Exception):
    pass

def check_semantics(node, expected_type=None):
    if node.type == 'binop':
        left_type = check_semantics(node.children[0])
        right_type = check_semantics(node.children[1])
        if left_type not in (INT_TYPE, FLOAT_TYPE) or right_type not in (INT_TYPE, FLOAT_TYPE):
            raise SemanticError(f"Error semántico: la operación {node.leaf} solo puede aplicarse a números")
        node.data_type = FLOAT_TYPE if FLOAT_TYPE in (left_type, right_type) else INT_TYPE
        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: la operación {node.leaf} devuelve {node.data_type} pero se esperaba {expected_type}")

    elif node.type == 'binlo':
        check_semantics(node.children[0], BOOL_TYPE)
        check_semantics(node.children[1], BOOL_TYPE)
        node.data_type = BOOL_TYPE
        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: la operación {node.leaf} devuelve {node.data_type} pero se esperaba {expected_type}")
    
    elif node.type == 'binco':
        left_type = check_semantics(node.children[0])
        right_type = check_semantics(node.children[1])
        if left_type not in (INT_TYPE, FLOAT_TYPE) or right_type not in (INT_TYPE, FLOAT_TYPE):
            raise SemanticError(f"Error semántico: la operación {node.leaf} solo puede aplicarse a números")
        node.data_type = BOOL_TYPE
        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: la operación {node.leaf} devuelve {node.data_type} pero se esperaba {expected_type}")

    elif node.type == 'num':
        if '.' in str(node.leaf):
            node.data_type = FLOAT_TYPE
        else:
            node.data_type = INT_TYPE
        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: el valor {node.leaf} es {node.data_type} pero se esperaba {expected_type}")

    elif node.type == 'bool':
        node.data_type = BOOL_TYPE
        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: el valor {node.leaf} es {node.data_type} pero se esperaba {expected_type}")

    elif node.type == 'func':
        if node.leaf in ('sin', 'cos', 'sqrt', 'exp'):
            arg_type = check_semantics(node.children[0])
            if arg_type not in (INT_TYPE, FLOAT_TYPE):
                raise SemanticError(f"Error semántico: el argumento de la función {node.leaf} debe ser numérico")
            node.data_type = FLOAT_TYPE
        elif node.leaf == 'log':
            arg1_type = check_semantics(node.children[0])
            arg2_type = check_semantics(node.children[1])
            if arg1_type not in (INT_TYPE, FLOAT_TYPE) or arg2_type not in (INT_TYPE, FLOAT_TYPE):
                raise SemanticError(f"Error semántico: los argumentos de la función {node.leaf} deben ser numéricos")
            node.data_type = FLOAT_TYPE
        elif node.leaf == 'rand':
            node.data_type = FLOAT_TYPE
        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: la función {node.leaf} devuelve {node.data_type} pero se esperaba {expected_type}")

    elif node.type == 'const':
        if node.leaf in ('PI', 'E'):
            node.data_type = FLOAT_TYPE
        else:
            raise SemanticError(f"Error semántico: constante desconocida {node.leaf}")
        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: el valor {node.leaf} es {node.data_type} pero se esperaba {expected_type}")

    elif node.type == 'string':
        node.data_type = STRING_TYPE
        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: el valor {node.leaf} es {node.data_type} pero se esperaba {expected_type}")

    elif node.type == 'concat':
        check_semantics(node.children[0], expected_type=STRING_TYPE)
        check_semantics(node.children[1], expected_type=STRING_TYPE)
        node.data_type = STRING_TYPE
        if expected_type and node.data_type != expected_type:
            raise SemanticError(f"Error semántico: la operación {node.leaf} devuelve {node.data_type} pero se esperaba {expected_type}")
    
    else:
        raise SemanticError(f"Tipo desconocido de nodo: {node.type}")
    
    if expected_type and node.data_type != expected_type:
        raise SemanticError(f"Error semántico: se esperaba {expected_type} pero se encontró {node.data_type}")

    return node.data_type

if __name__ == "__main__":
    from my_parser import parser

    test_data = [
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
        try:
            result = parser.parse(data)
            if result:
                check_semantics(result)
                print("Semantics check passed")
                print(result)
        except SemanticError as e:
            print(f"Semantic error: {e}")
        except Exception as e:
            print(f"Syntax or other error: {e}")
