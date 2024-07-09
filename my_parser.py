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

        program = self.G.NonTerminal('<program>', startSymbol=True)
        stats, specialBlock = self.G.NonTerminals(
            '<stats> <specialBlock>')
        expr, blockExpr = self.G.NonTerminals(
            '<expr> <blockExpr>')
        asig_list, asig1 = self.G.NonTerminals(
            '<asig_list> <asig1>')
        atom, idnode, specialBlock_list = self.G.NonTerminals(
            '<atom> <idnode> <specialBlock_list>')
        subexpr, expr, term, factor, atom = self.G.NonTerminals(
            '<subexpr> <expr> <term> <factor> <atom>')
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

        program %= stats + specialBlock, lambda h, s: ProgramNode(s[1], s[2])
        stats %= self.G.Epsilon, lambda h, s: []

        # # ************ Producciones de Protocols ************
        # # Protocolo completo
        # stats %= protocol + idx + extension + obrace + protocolBody + cbrace + stats, lambda h,s:[ProtocolNode(s[2],s[3],s[5])] + s[7]
        # # Herencia
        # extension %= extends + idx, lambda h,s: s[2]
        # extension %= self.G.Epsilon, lambda h,s:None
        # # Cuerpo de un protocolo
        # protocolBody %= idx + opar + arg_typed_list + cpar + colon + idx + semicolon + protocolBody, lambda h,s: [MethodProtocolNode(s[1],s[3],s[6])] + s[8]
        # protocolBody %= self.G.Epsilon, lambda h,s:[]

        # *************** Producciones de Functions ***************
        # Function
        stats %= functionx + idx + opar + arg_opt_typed + cpar + opt_typed + func_body + stats, lambda h, s: [FuncDeclarationNode(s[2], s[7], s[4], s[6])] + s[8]
        # Cuerpo de un function
        func_body %= arrow + expr + semicolon, lambda h, s: s[2]
        func_body %= blockExpr, lambda h, s: s[1]

        # *************** Producciones de Type ****************
        stats %= typex + idx + arg_opt_typed_list + inherit_item + obrace + type_body + cbrace + stats, lambda h,s: [TypeDeclarationNode(s[2],TypeBodyDeclarationNode(s[6][0],s[6][1]),s[3],s[4][0],s[4][1])]+s[8]
        # Manejar la herencia
        inherit_item %= inherits + idx, lambda h,s: (s[2],[])
        inherit_item %= inherits + idx + opar + arg_expr + cpar, lambda h,s: (s[2],s[4])
        inherit_item %= self.G.Epsilon, lambda h,s: (None,[])
        # Cuerpo de un Type
        type_body %= attribute_declaration + type_body, lambda h,s: ([s[1]]+s[2][0],s[2][1])
        type_body %= method_declaration + type_body, lambda h,s: (s[2][0],[s[1]]+s[2][1])
        type_body %= self.G.Epsilon, lambda h,s: ([],[])
        # Atributos de Type
        attribute_declaration %= idnode + opt_typed + asign1 + expr + semicolon, lambda h,s: AttributeNode(s[1],s[4],s[2])
        # Métodos de Type
        method_declaration %= idx + opar + arg_opt_typed + cpar + opt_typed + func_body, lambda h,s:MethodNode(s[1], s[6], s[3], s[5])

        # Lista de parámetros opcionalmente tipados
        arg_opt_typed_list %= self.G.Epsilon, lambda h,s:[]
        arg_opt_typed_list %= opar + arg_opt_typed + cpar, lambda h,s:s[2]
        arg_opt_typed %= idx + opt_typed, lambda h,s:[(s[1],s[2])]
        arg_opt_typed %= idx + opt_typed + comma + arg_opt_typed, lambda h,s:[(s[1],s[2])] + s[4]
        arg_opt_typed %= self.G.Epsilon, lambda h,s:[]

        opt_typed %= colon + idx, lambda h, s: s[2]
        opt_typed %= self.G.Epsilon, lambda h, s: None

        arg_typed_list %= idx + colon + idx, lambda h,s:[(s[1],s[3])]
        arg_typed_list %= idx + colon + idx + comma + arg_typed_list, lambda h,s:[(s[1],s[3])] + s[5]
        
        # Lista de Variables
        arg_list %= idnode, lambda h, s: [s[1]]
        arg_list %= idnode + comma + arg_list, lambda h, s: [s[1]] + s[3]

        # Lista de Expresiones
        arg_expr %= expr, lambda h, s: [s[1]]
        arg_expr %= expr + comma + arg_expr, lambda h, s: [s[1]] + s[3]

        # Bloques especiales
        specialBlock %= expr + semicolon, lambda h, s: s[1]
        specialBlock %= blockExpr, lambda h, s: s[1]
        blockExpr %= obrace + specialBlock_list + cbrace, lambda h, s: BlockNode(s[2])

        # Lista de bloques especiales
        specialBlock_list %= specialBlock, lambda h, s: [s[1]]
        specialBlock_list %= specialBlock + specialBlock_list, lambda h, s: [s[1]] + s[2]

        # ***************** Expresiones ******************
        expr %= blockExpr, lambda h, s: s[1]
        # expr %= let + asig_list + inx + expr, lambda h, s: LetNode(s[2], s[4])
        expr %= let + asig_list + inx + expr, lambda h, s: MultipleLet(s)
        expr %= ifx + opar + expr + cpar + specialBlock + elifx_expr + elsex + superexpr, lambda h, s: IfNode(s[3], s[5], s[8], s[6][0], s[6][1])
        expr %= whilex + opar + expr + cpar + expr, lambda h, s: WhileNode(s[3], s[5])
        expr %= forx + opar + idnode + inx + rangex + opar + expr + comma + expr + cpar + cpar + expr, lambda h, s: ForRangeToWhile(s)
        expr %= forx + opar + idnode + inx + idnode + cpar + expr, lambda h, s: ForToWhile(s)
        expr %= printx + opar + expr + cpar, lambda h, s: PrintNode(s[3])
        expr %= idnode + asign2 + expr, lambda h, s: DestructNode(s[1], s[3])
        expr %= new + idx + opar + arg_expr + cpar, lambda h, s: ObjectCreationNode(s[2], s[4])
        expr %= new + idx + opar + cpar, lambda h, s: ObjectCreationNode(s[2], [])
        expr %= subexpr, lambda h, s: s[1]

        superexpr %= expr, lambda h, s: s[1]
        superexpr %= obrace + cbrace, lambda h, s: None

        elifx_expr %= elifx + opar + expr + cpar + specialBlock + elifx_expr, lambda h, s: (s[6][0]+[s[3]], s[6][1]+[s[5]])
        elifx_expr %= self.G.Epsilon, lambda h, s: ([], [])

        asig_list %= asig1, lambda h, s: [s[1]]
        asig_list %= asig1 + comma + asig_list, lambda h, s: [s[1]] + s[3]
        asig1 %= idnode + opt_typed + asign1 + expr, lambda h, s: AssignNode(s[1], s[4], s[2])

        # Aritmetica
        subexpr %= subexpr + plus + term, lambda h, s: PlusNode(s[1], s[3])
        subexpr %= subexpr + minus + term, lambda h, s: MinusNode(s[1], s[3])
        subexpr %= subexpr + andx + term, lambda h, s: AndNode(s[1], s[3])
        subexpr %= subexpr + orx + term, lambda h, s: OrNode(s[1], s[3])
        # subexpr %= notx + term, lambda h, s: NotNode(s[2])
        subexpr %= subexpr + eq + term, lambda h, s: EQNode(s[1], s[3])
        subexpr %= subexpr + ne + term, lambda h, s: NENode(s[1], s[3])
        subexpr %= subexpr + gt + term, lambda h, s: GTNode(s[1], s[3])
        subexpr %= subexpr + lt + term, lambda h, s: LTNode(s[1], s[3])
        subexpr %= subexpr + ge + term, lambda h, s: GENode(s[1], s[3])
        subexpr %= subexpr + le + term, lambda h, s: LENode(s[1], s[3])
        subexpr %= subexpr + concat + term, lambda h, s: ConcatNode(s[1], s[3])
        subexpr %= subexpr + concat_space + term, lambda h, s: ConcatSpaceNode(s[1], s[3])
        subexpr %= term, lambda h, s: s[1]

        term %= term + star + factor, lambda h, s: StarNode(s[1], s[3])
        term %= term + div + factor, lambda h, s: DivNode(s[1], s[3])
        # term %= term + powx + factor, lambda h, s: PowNode(s[1], s[3])
        term %= term + mod + factor, lambda h, s: ModNode(s[1], s[3])
        term %= factor, lambda h, s: s[1]

        # factor %= sin + opar + expr + cpar, lambda h, s: SinNode(s[3])
        # factor %= cos + opar + expr + cpar, lambda h, s: CosNode(s[3])
        # factor %= sqrt + opar + expr + cpar, lambda h, s: SqrtNode(s[3])
        # factor %= exp + opar + expr + cpar, lambda h, s: ExpNode(s[3])
        # factor %= log + opar + expr + comma + expr + cpar, lambda h, s: LogNode(s[3], s[5])
        # factor %= rand + opar + cpar, lambda h, s: RandNode()
        factor %= atom, lambda h, s: s[1]

        atom %= number, lambda h, s: NumberNode(s[1])
        # atom %= true, lambda h, s: BoolNode(s[1])
        # atom %= false, lambda h, s: BoolNode(s[1])
        # atom %= pi, lambda h, s: NumberNode(s[1])
        # atom %= e, lambda h, s: NumberNode(s[1])
        atom %= string, lambda h, s: StringNode(s[1])
        atom %= opar + expr + cpar, lambda h, s: s[2]
        atom %= selfx + dot + idnode, lambda h, s: SelfNode(s[3])
        atom %= selfx + dot + idx + dot + recurrent_object, lambda h, s: SelfNode(IdentifierNode(s[3],s[5]))
        atom %= selfx + dot + recurrent_object, lambda h, s: SelfNode(s[3])
        atom %= obrake + arg_expr + cbrake, lambda h, s: VectorNode(s[2])
        atom %= idnode, lambda h, s: s[1]
        atom %= idx + dot + recurrent_object, lambda h, s: IdentifierNode(s[1], s[3])
        atom %= recurrent_object, lambda h, s: s[1]

        recurrent_object %= idx + opar + arg_expr + cpar + dot + recurrent_object, lambda h, s: CallNode(s[1], s[3], s[6])
        recurrent_object %= idx + opar + cpar + dot + recurrent_object, lambda h, s: CallNode(s[1], [], s[5])
        recurrent_object %= idx + opar + arg_expr + cpar, lambda h, s: CallNode(s[1], s[3])
        recurrent_object %= idx + opar + cpar, lambda h, s: CallNode(s[1])

        idnode %= idx, lambda h, s: IdentifierNode(s[1])

        #############################################################################

        lexer = Lexer('eof', self.terminals)

        tokens = lexer(text)

        ###################################################################################

        parser = LR1Parser(self.G, 'parser_autom')

        derivations,msg = parser([tok.token_type for tok in tokens])
        self.error_msg = msg
        
        if derivations is None:
            self.ast = None
            return
            
        tokens.reverse()
        derivations.reverse()

        self.ast = evaluate_parse(derivations, tokens)

    def __repr__(self):
        from utils.my_format_visitor import FormatVisitor

        formatter = FormatVisitor()
        tree = formatter.visit(self.ast)
        return tree


if __name__ == "__main__":

    text = '''
            let a=4,b=3 in {
                print(a);
            };
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
