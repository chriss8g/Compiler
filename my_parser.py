import ply.yacc as yacc
from lexer import tokens
from my_ast import ASTNode

def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = ASTNode(type='binop', children=[p[1], p[3]], leaf=p[2])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    p[0] = ASTNode(type='binop', children=[p[1], p[3]], leaf=p[2])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = ASTNode(type='num', leaf=p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error():
    print("Error de sintaxis")

parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result.print())
