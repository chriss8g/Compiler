import os
import pickle
from utils.pycompiler import *
from parser.TreeDef import *
from nodes_types.hulk_types import *
from my_lexer import Lexer
if os.path.exists('./parser/action'):
    from parser.tools_saved import *
else:
    from parser.tools import *

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
    
    if len(assign_list) > 1:
        let = LetNode([assign_list[0]],None)
        tmp = let
        for i in range(1,len(assign_list)-1):
            tmp.body = LetNode([assign_list[i]],None)
            tmp = tmp.body
        tmp.body = LetNode([assign_list[len(assign_list)-1]],s[4])
        return let
    

    return LetNode([assign_list[0]],s[4])


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

        atributes = [
            # Programa
            lambda h, s: ProgramNode(s[1], s[2]),
            lambda h, s: [],
            
            # Protocolos
            lambda h,s:[ProtocolNode(s[2],s[3],s[5])] + s[7],
            lambda h,s: s[2],
            lambda h,s:None,
            lambda h,s: [MethodProtocolNode(s[1],s[3],s[6])] + s[8],
            lambda h,s:[],
            
            # Funciones
            lambda h, s: [FuncDeclarationNode(s[2], s[7], s[4], s[6])] + s[8],
            lambda h, s: s[2],
            lambda h, s: s[1],
            
            # Tipos
            lambda h,s: [TypeDeclarationNode(s[2],TypeBodyDeclarationNode(s[6][0],s[6][1]),s[3],s[4][0],s[4][1])]+s[8],
            lambda h,s: (s[2],[]),
            lambda h,s: (s[2],s[4]),
            lambda h,s: (None,[]),
            lambda h,s: ([s[1]]+s[2][0],s[2][1]),
            lambda h,s: (s[2][0],[s[1]]+s[2][1]),
            lambda h,s: ([],[]),
            lambda h,s: AttributeNode(IdentifierNode(s[1],None,s[2]),s[4],s[2]),
            lambda h,s:MethodNode(s[1], s[6], s[3], s[5]),
            
            # Lista de parámetros opcionalmente tipados
            lambda h,s:[],
            lambda h,s:s[2],
            lambda h,s:[(s[1],s[2])],
            lambda h,s:[(s[1],s[2])] + s[4],
            lambda h,s:[],
            
            # Tipado opcional
            lambda h, s: s[2],
            lambda h, s: None,
            
            # Lista de parametros con tipado obligatorio
            lambda h,s:[],
            lambda h,s:[(s[1],s[3])],
            lambda h,s:[(s[1],s[3])] + s[5],
            
            # Lista de variables
            lambda h, s: [s[1]],
            lambda h, s: [s[1]] + s[3],
            
            # Lista de expresiones
            lambda h, s: [s[1]],
            lambda h, s: [s[1]] + s[3],
            
            # Bloques especiales
            lambda h, s: s[1],
            lambda h, s: s[1],
            lambda h, s: BlockNode(s[2]),
            
            # Lista de bloques especiales
            lambda h, s: [s[1]],
            lambda h, s: [s[1]] + s[2],
            
            # Expresiones
            lambda h, s: s[1],
            lambda h, s: MultipleLet(s),
            lambda h, s: IfNode(s[3], s[5], s[8], s[6][0], s[6][1]),
            lambda h, s: WhileNode(s[3], s[5]),
            lambda h, s: ForRangeToWhile(s),
            lambda h, s: ForToWhile(s),
            lambda h, s: PrintNode(s[3]),
            lambda h, s: DestructNode(s[1], s[3]),
            lambda h, s: ObjectCreationNode(s[2], s[4]),
            lambda h, s: ObjectCreationNode(s[2], []),
            lambda h, s: s[1],
            
            # Super expresion
            lambda h, s: s[1],
            lambda h, s: None,
            
            # Elif cuerpo
            lambda h, s: (s[6][0]+[s[3]], s[6][1]+[s[5]]),
            lambda h, s: ([], []),
            
            # Lista de asignaciones para el let
            lambda h, s: [s[1]],
            lambda h, s: [s[1]] + s[3],
            lambda h, s: AssignNode(s[1], s[4], s[2]),
            
            # Aritmetica
            lambda h, s: PlusNode(s[1], s[3]),
            lambda h, s: MinusNode(s[1], s[3]),
            lambda h, s: AndNode(s[1], s[3]),
            lambda h, s: OrNode(s[1], s[3]),
            lambda h, s: NotNode(s[2]),
            lambda h, s: EQNode(s[1], s[3]),
            lambda h, s: NENode(s[1], s[3]),
            lambda h, s: GTNode(s[1], s[3]),
            lambda h, s: LTNode(s[1], s[3]),
            lambda h, s: GENode(s[1], s[3]),
            lambda h, s: LENode(s[1], s[3]),
            lambda h, s: ConcatNode(s[1], s[3]),
            lambda h, s: ConcatSpaceNode(s[1], s[3]),
            lambda h, s: s[1],
            
            # Terminos
            lambda h, s: StarNode(s[1], s[3]),
            lambda h, s: DivNode(s[1], s[3]),
            lambda h, s: PowNode(s[1], s[3]),
            lambda h, s: ModNode(s[1], s[3]),
            lambda h, s: s[1],
            
            # Factor
            lambda h, s: SinNode(s[3]),
            lambda h, s: CosNode(s[3]),
            lambda h, s: SqrtNode(s[3]),
            lambda h, s: ExpNode(s[3]),
            lambda h, s: LogNode(s[3], s[5]),
            lambda h, s: RandNode(),
            lambda h, s: s[1],
            
            # Atom
            lambda h, s: NumberNode(s[1]),
            lambda h, s: BoolNode(s[1]),
            lambda h, s: BoolNode(s[1]),
            lambda h, s: NumberNode(s[1]),
            lambda h, s: NumberNode(s[1]),
            lambda h, s: StringNode(s[1]),
            lambda h, s: s[2],
            lambda h, s: SelfNode(s[3]),
            lambda h, s: SelfNode(IdentifierNode(s[3],s[5])),
            lambda h, s: SelfNode(s[3]),
            lambda h, s: VectorNode(s[2]),
            lambda h, s: s[1],
            lambda h, s: IdentifierNode(s[1], s[3]),
            lambda h, s: s[1],
            
            # Objetos recurrentes
            lambda h, s: CallNode(s[1], s[3], s[6]),
            lambda h, s: CallNode(s[1], [], s[5]),
            lambda h, s: CallNode(s[1], s[3]),
            lambda h, s: CallNode(s[1]),
            
            # Idnode
            lambda h, s: IdentifierNode(s[1])
        ]

        program %= stats + specialBlock
        stats %= self.G.Epsilon

        # ************ Producciones de Protocols ************
        # Protocolo completo
        stats %= protocol + idx + extension + obrace + protocolBody + cbrace + stats
        # Herencia
        extension %= extends + idx
        extension %= self.G.Epsilon
        # Cuerpo de un protocolo
        protocolBody %= idx + opar + arg_typed_list + cpar + colon + idx + semicolon + protocolBody
        protocolBody %= self.G.Epsilon

        # *************** Producciones de Functions ***************
        # Function
        stats %= functionx + idx + opar + arg_opt_typed + cpar + opt_typed + func_body + stats
        # Cuerpo de un function
        func_body %= arrow + expr + semicolon
        func_body %= blockExpr

        # *************** Producciones de Type ****************
        stats %= typex + idx + arg_opt_typed_list + inherit_item + obrace + type_body + cbrace + stats
        # Manejar la herencia
        inherit_item %= inherits + idx
        inherit_item %= inherits + idx + opar + arg_expr + cpar
        inherit_item %= self.G.Epsilon
        # Cuerpo de un Type
        type_body %= attribute_declaration + type_body
        type_body %= method_declaration + type_body
        type_body %= self.G.Epsilon
        # Atributos de Type
        attribute_declaration %= idx + opt_typed + asign1 + expr + semicolon
        # Métodos de Type
        method_declaration %= idx + opar + arg_opt_typed + cpar + opt_typed + func_body

        # Lista de parámetros opcionalmente tipados
        arg_opt_typed_list %= self.G.Epsilon
        arg_opt_typed_list %= opar + arg_opt_typed + cpar
        arg_opt_typed %= idx + opt_typed
        arg_opt_typed %= idx + opt_typed + comma + arg_opt_typed
        arg_opt_typed %= self.G.Epsilon

         # Tipado opcional
        opt_typed %= colon + idx
        opt_typed %= self.G.Epsilon

        # Lista de parametros con tipado obligatorio
        arg_typed_list %= self.G.Epsilon
        arg_typed_list %= idx + colon + idx
        arg_typed_list %= idx + colon + idx + comma + arg_typed_list
        
        # Lista de Variables
        arg_list %= idnode
        arg_list %= idnode + comma + arg_list

        # Lista de Expresiones
        arg_expr %= expr
        arg_expr %= expr + comma + arg_expr

        # Bloques especiales
        specialBlock %= expr + semicolon
        specialBlock %= blockExpr
        blockExpr %= obrace + specialBlock_list + cbrace

        # Lista de bloques especiales
        specialBlock_list %= specialBlock
        specialBlock_list %= specialBlock + specialBlock_list

        # ***************** Expresiones ******************
        expr %= blockExpr
        expr %= let + asig_list + inx + expr
        expr %= ifx + opar + expr + cpar + specialBlock + elifx_expr + elsex + superexpr
        expr %= whilex + opar + expr + cpar + expr
        expr %= forx + opar + idnode + inx + rangex + opar + expr + comma + expr + cpar + cpar + expr
        expr %= forx + opar + idnode + inx + idnode + cpar + expr
        expr %= printx + opar + expr + cpar
        expr %= idnode + asign2 + expr
        expr %= new + idx + opar + arg_expr + cpar
        expr %= new + idx + opar + cpar
        expr %= subexpr

        # Super expresion
        superexpr %= expr
        superexpr %= obrace + cbrace

        # Cuerpo del elif
        elifx_expr %= elifx + opar + expr + cpar + specialBlock + elifx_expr
        elifx_expr %= self.G.Epsilon

        # Lista de asignaciones para el let
        asig_list %= asig1
        asig_list %= asig1 + comma + asig_list
        asig1 %= idnode + opt_typed + asign1 + expr

        # Aritmetica
        subexpr %= subexpr + plus + term
        subexpr %= subexpr + minus + term
        subexpr %= subexpr + andx + term
        subexpr %= subexpr + orx + term
        subexpr %= notx + term
        subexpr %= subexpr + eq + term
        subexpr %= subexpr + ne + term
        subexpr %= subexpr + gt + term
        subexpr %= subexpr + lt + term
        subexpr %= subexpr + ge + term
        subexpr %= subexpr + le + term
        subexpr %= subexpr + concat + term
        subexpr %= subexpr + concat_space + term
        subexpr %= term

        term %= term + star + factor
        term %= term + div + factor
        term %= term + powx + factor
        term %= term + mod + factor
        term %= factor

        factor %= sin + opar + expr + cpar
        factor %= cos + opar + expr + cpar
        factor %= sqrt + opar + expr + cpar
        factor %= exp + opar + expr + cpar
        factor %= log + opar + expr + comma + expr + cpar
        factor %= rand + opar + cpar
        factor %= atom

        atom %= number
        atom %= true
        atom %= false
        atom %= pi
        atom %= e
        atom %= string
        atom %= opar + expr + cpar
        atom %= selfx + dot + idnode
        atom %= selfx + dot + idx + dot + recurrent_object
        atom %= selfx + dot + recurrent_object
        atom %= obrake + arg_expr + cbrake
        atom %= idnode
        atom %= idx + dot + recurrent_object
        atom %= recurrent_object

        recurrent_object %= idx + opar + arg_expr + cpar + dot + recurrent_object
        recurrent_object %= idx + opar + cpar + dot + recurrent_object
        recurrent_object %= idx + opar + arg_expr + cpar
        recurrent_object %= idx + opar + cpar

        idnode %= idx

        #############################################################################

        lexer = Lexer('eof', self.terminals)

        tokens = lexer(text)

        ###################################################################################

        parser = LR1Parser(self.G, 'parser')

        derivations,msg = parser([tok.token_type for tok in tokens])
        self.error_msg = msg
        
        if not derivations:
            self.ast = None
            return
            
        tokens.reverse()
        derivations.reverse()

        self.ast = evaluate_parse(derivations, tokens, self.G, atributes)

    def __repr__(self):
        from utils.my_format_visitor import FormatVisitor

        formatter = FormatVisitor()
        tree = formatter.visit(self.ast)
        return tree


if __name__ == "__main__":

    text = '''
            type lala {
                a = 0;
                lalal (x) => !x;
            }
            let a = new lala() in print(a.lalal(5));
        '''

    codeToAST = CodeToAST(text)

    if codeToAST.ast:
        print(codeToAST)
    else:
        print(codeToAST.error_msg)

    # # Especifica la ruta del archivo donde quieres escribir
    # ruta_del_archivo = "tests/parser/expected_out/test_18.txt"

    # # Abre el archivo en modo de escritura ('w')
    # with open(ruta_del_archivo, 'w') as archivo:
    #     # Escribe el string en el archivo
    #     archivo.write(repr(codeToAST))
