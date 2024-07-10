import os
import pickle
from utils.pycompiler import *
from parser.TreeDef import *
from parser.tools import *
from nodes_types.hulk_types import *
from my_lexer import Lexer


def ForRangeToWhile(s):
    count = s[3]
    start = s[7]
    end = s[9]
    body = []
    if isinstance(s[12], list):
        for expr in s[12]:
            body.append(expr)
    else:
        body.append(s[12])

    increase_count = DestructNode(count, PlusNode(count, NumberNode(1)))
    body.append(increase_count)
    assign = AssignNode(count, start)
    while_term = WhileNode(LTNode(count, end), BlockNode(body))
    let_term = LetNode([assign], while_term)
    # return let_term
    return let_term

def ForToWhile(s):
    # expr %= forx + opar + idnode + inx + idnode + cpar + expr, lambda h, s: ForToWhile(s)
    
    nextx = CallNode('next')
    current = CallNode('current')
    arr_next = IdentifierNode(s[5].name,nextx)
    arr_current = IdentifierNode(s[5].name,current)
    body = s[7]
    assig = AssignNode(s[3],arr_current)
    let = LetNode([assig],body)
    whilex = WhileNode(arr_next,let)
    return whilex

def MultipleLet(s):
    # expr %= let + asig_list + inx + expr, lambda h, s: LetNode(s[2], s[4])
    
    assign_list = s[2]
    let = LetNode([assign_list[0]],None)
    tmp = let
    for i in range(1,len(assign_list)-1):
        tmp.body = LetNode([assign_list[i]],None)
        tmp = tmp.body
    
    tmp.body = LetNode([assign_list[len(assign_list)-1]],s[4])
    return let


class CodeToAST:

    def __init__(self, text):
        self.G = Grammar()

        # Definir los terminales
        let, functionx, inx = self.G.Terminals('let function in')
        printx, sin, cos, sqrt, exp, log, rand = self.G.Terminals(
            'print sin cos sqrt exp log rand')
        semicolon, colon, comma, opar, cpar, arrow = self.G.Terminals(
            '; : , ( ) =>')
        asign1, plus, minus, star, div = self.G.Terminals('= + - * /')
        powx, mod, andx, orx, notx = self.G.Terminals('^ % & | !')
        eq, gt, lt, ge, le = self.G.Terminals('== > < >= <=')
        ne, concat, obrace, cbrace, asign2 = self.G.Terminals('!= @ { } :=')
        pi, e, true, false = self.G.Terminals('PI E true false')
        idx, number, string = self.G.Terminals('id num string')
        ifx, elsex, elifx, whilex, forx, rangex = self.G.Terminals(
            'if else elif while for range')
        typex, inherits = self.G.Terminals('type inherits')
        selfx, new, extends = self.G.Terminals('self new extends')
        dot, concat_space, returnx = self.G.Terminals('. @@ return')
        obrake, cbrake, protocol = self.G.Terminals('[ ] protocol')

        program, blockExpr = self.G.NonTerminals('<program>  <blockExpr>')
        stats, specialBlock = self.G.NonTerminals(
            '<stats> <specialBlock>')
        expr = self.G.NonTerminal(
            '<expr>', startSymbol=True)
        asig_list, asig1 = self.G.NonTerminals(
            '<asig_list> <asig1>')
        atom, idnode, specialBlock_list = self.G.NonTerminals(
            '<atom> <idnode> <specialBlock_list>')
        subexpr, term, factor, atom = self.G.NonTerminals(
            '<subexpr> <term> <factor> <atom>')
        extension, protocolBody = self.G.NonTerminals(
            '<extension> <protocolBody>')
        type_body, inherit_item = self.G.NonTerminals(
            '<type_body> <inherit_item>')
        arg_list, func_body, arg_expr, arg_opt_typed = self.G.NonTerminals(
            '<arg_list> <func_body> <arg_expr> <arg_opt_typed>')
        attribute_declaration, method_declaration = self.G.NonTerminals(
            '<attribute_declaration> <method_declaration>')
        opt_typed, arg_opt_typed_list, elifx_expr = self.G.NonTerminals(
            '<opt_typed> <arg_opt_typed_list> <elifx_expr>')
        recurrent_object, superexpr, arg_typed_list = self.G.NonTerminals(
            '<recurrent_object> <superexpr> <arg_typed_list>')

        terminals = {}
        terminals['let'] = let
        terminals['function'] = functionx
        terminals['in'] = inx
        terminals['print'] = printx
        terminals['sin'] = sin
        terminals['cos'] = cos
        terminals['sqrt'] = sqrt
        terminals['exp'] = exp
        terminals['log'] = log
        terminals['rand'] = rand
        terminals['semi'] = semicolon
        terminals['colon'] = colon
        terminals['comma'] = comma
        terminals['opar'] = opar
        terminals['cpar'] = cpar
        terminals['arrow'] = arrow
        terminals['asign1'] = asign1
        terminals['plus'] = plus
        terminals['minus'] = minus
        terminals['star'] = star
        terminals['divide'] = div
        terminals['pow'] = powx
        terminals['mod'] = mod
        terminals['and'] = andx
        terminals['or'] = orx
        terminals['not'] = notx
        terminals['eq'] = eq
        terminals['gt'] = gt
        terminals['lt'] = lt
        terminals['ge'] = ge
        terminals['le'] = le
        terminals['ne'] = ne
        terminals['concat'] = concat
        terminals['lbrace'] = obrace
        terminals['rbrace'] = cbrace
        terminals['lbrake'] = obrake
        terminals['rbrake'] = cbrake
        terminals['asign2'] = asign2
        terminals['PI'] = pi
        terminals['E'] = e
        terminals['true'] = true
        terminals['false'] = false
        terminals['id'] = idx
        terminals['num'] = number
        terminals['string'] = string
        terminals['if'] = ifx
        terminals['else'] = elsex
        terminals['elif'] = elifx
        terminals['while'] = whilex
        terminals['for'] = forx
        terminals['range'] = rangex
        terminals['type'] = typex
        terminals['inherits'] = inherits
        terminals['self'] = selfx
        terminals['new'] = new
        terminals['dot'] = dot
        terminals['protocol'] = protocol
        terminals['extends'] = extends
        terminals['concat_space'] = concat_space
        terminals['return'] = returnx
        terminals['eof'] = self.G.EOF

        self.terminals = terminals
        
        attributes = [
            lambda h, s: AssignNode(s[1],s[3]),
            lambda h, s: NumberNode(s[1]),
            lambda h,s:PlusNode(NumberNode(s[1]),s[3]),
            lambda h, s: NumberNode(s[1])
        ]

        expr %= atom + asign1 + atom 
        expr %= number
        atom %= number + plus + atom
        atom %= number

        #############################################################################

        lexer = Lexer('eof', self.terminals)

        tokens = lexer(text)

        ###################################################################################

        parser = LR1Parser(self.G,"parser")

        derivations,msg = parser([tok.token_type for tok in tokens])
        self.error_msg = msg
        
        if derivations is None:
            self.ast = None
            return
            
        tokens.reverse()
        derivations.reverse()

        self.ast = evaluate_parse(derivations, tokens, self.G, attributes)

    def __repr__(self):
        from utils.my_format_visitor import FormatVisitor

        formatter = FormatVisitor()
        tree = formatter.visit(self.ast)
        return tree


if __name__ == "__main__":

    text = '''
            3+4=1
        '''

    codeToAST = CodeToAST(text)

    if codeToAST.error_msg == 'Clean Code':
        print(codeToAST)
    else:
        print(codeToAST.error_msg)

    # # Especifica la ruta del archivo donde quieres escribir
    # ruta_del_archivo = "tests/parser/expected_out/test_18.txt"

    # # Abre el archivo en modo de escritura ('w')
    # with open(ruta_del_archivo, 'w') as archivo:
    #     # Escribe el string en el archivo
    #     archivo.write(repr(codeToAST))
