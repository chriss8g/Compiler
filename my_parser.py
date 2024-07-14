import os
import pickle
from utils.pycompiler import *
from parser.TreeDef import *
from nodes_types.hulk_types import *
from my_lexer import Lexer
if os.path.exists('./parser/action') and os.path.exists('./parser/goto'):
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

    minus = AssignNode(count, MinusNode(count, NumberNode(1)))

    increase_count = DestructNode(count, PlusNode(count, NumberNode(1)))
    # body.append(increase_count)
    assign = AssignNode(count, start)
    while_term = WhileNode(LTNode(increase_count, end), BlockNode(body))
    let_term = LetNode([assign], BlockNode([minus, while_term]))
    return let_term

def ForToWhile(s):
    # expr %= forx + opar + idnode + inx + idnode + cpar + expr, lambda h, s: ForToWhile(s)
    
    nextx = CallNode('next')
    current = CallNode('current')
    arr_next = IdentifierNode(s[5].name,nextx)
    arr_current = IdentifierNode(s[5].name,current)
    body = s[7]
    assig = AssignNode(s[3],arr_current)
    let = LetNode([assig],body, line=s[1].line)
    whilex = WhileNode(arr_next,let, line=s[1])
    return whilex

def MultipleLet(s):
    # expr %= let + asig_list + inx + expr, lambda h, s: LetNode(s[2], s[4])
    
    assign_list = s[2]
    
    if len(assign_list) > 1:
        let = LetNode([assign_list[0]],None, line = s[1].line)
        tmp = let
        for i in range(1,len(assign_list)-1):
            tmp.body = LetNode([assign_list[i]],None, line=s[1].line)
            tmp = tmp.body
        tmp.body = LetNode([assign_list[len(assign_list)-1]],s[4], line=s[1].line)
        return let
    

    return LetNode([assign_list[0]],s[4], line=s[1].line)


class CodeToAST:

    def __init__(self, text):
        self.G = Grammar()

        # Definir los terminales
        let, functionx, inx = self.G.Terminals('let function in')
        printx, sin, cos, sqrt, exp, log, rand = self.G.Terminals(
            'print sin cos sqrt exp log rand')
        semicolon, colon, comma, opar, cpar, arrow = self.G.Terminals(
            '; : , ( ) =>')
        asign1, plus, minus, star, star2, div = self.G.Terminals('= + - * ** /')
        powx, mod, andx, andx2, orx, orx2, notx = self.G.Terminals('^ % & | and or !')
        eq, gt, lt, ge, le = self.G.Terminals('== > < >= <=')
        ne, concat, obrace, cbrace, asign2 = self.G.Terminals('!= @ { } :=')
        pi, e, true, false = self.G.Terminals('PI E true false')
        idx, number, string = self.G.Terminals('id num string')
        ifx, elsex, elifx, whilex, forx, rangex = self.G.Terminals(
            'if else elif while for range')
        typex, inherits, isx, asx = self.G.Terminals('type inherits is as')
        new, extends = self.G.Terminals('new extends')
        dot, concat_space, returnx = self.G.Terminals('. @@ return')
        obrake, cbrake, protocol, implicit = self.G.Terminals('[ ] protocol implicit')

        program = self.G.NonTerminal('<program>', startSymbol=True)
        stats, specialBlock = self.G.NonTerminals(
            '<stats> <specialBlock>')
        expr, blockExpr = self.G.NonTerminals(
            '<expr> <blockExpr>')
        asig_list, asig1 = self.G.NonTerminals(
            '<asig_list> <asig1>')
        idnode, specialBlock_list = self.G.NonTerminals(
            '<idnode> <specialBlock_list>')
        calc_expr = self.G.NonTerminal(
            '<calc_expr>')
        string_expr, string_factor = self.G.NonTerminals(
            '<string_expr> <string_factor>')
        logical_expr, logical_term, logical_factor, comparative_expr = self.G.NonTerminals(
            '<logical_expr> <logical_term> <logical_factor> <comparative_expr>')
        aritmetic_expr, aritmetic_term, aritmetic_factor, aritmetic_atom, self_expr = self.G.NonTerminals(
            '<aritmetic_expr> <aritmetic_term> <aritmetic_factor> <aritmetic_atom> <self_expr>')
        extension, protocolBody = self.G.NonTerminals(
            '<extension> <protocolBody> ')
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
        terminals['or2'] = orx2
        terminals['and2'] = andx2
        terminals['cpar'] = cpar
        terminals['arrow'] = arrow
        terminals['asign1'] = asign1
        terminals['plus'] = plus
        terminals['minus'] = minus
        terminals['star'] = star
        terminals['divide'] = div
        terminals['pow'] = powx
        terminals['mod'] = mod
        terminals['is'] = isx
        terminals['as'] = asx
        terminals['and'] = andx
        terminals['or'] = orx
        terminals['not'] = notx
        terminals['eq'] = eq
        terminals['implicit'] = implicit
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
        terminals['star2'] = star2
        terminals['if'] = ifx
        terminals['else'] = elsex
        terminals['elif'] = elifx
        terminals['while'] = whilex
        terminals['for'] = forx
        terminals['range'] = rangex
        terminals['type'] = typex
        terminals['inherits'] = inherits
        # terminals['self'] = selfx
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
            lambda h, s: ProgramNode(s[1]+s[3], s[2]),
            lambda h, s: [],
            
            # Protocolos
            lambda h,s:[ProtocolNode(s[2].lex,s[3],s[5], line=s[1].line)] + s[7],
            lambda h,s: s[2].lex,
            lambda h,s:None,
            lambda h,s: [MethodProtocolNode(s[1].lex,s[3],s[6].lex, line=s[1].line)] + s[8],
            lambda h,s:[],
            
            # Funciones
            lambda h, s: [FuncDeclarationNode(s[2].lex, s[7], s[4], s[6], line=s[1].line)] + s[8],
            lambda h, s: s[2],
            lambda h, s: s[1],
            
            # Tipos
            lambda h,s: [TypeDeclarationNode(s[2].lex,TypeBodyDeclarationNode(s[6][0],s[6][1]),s[3],s[4][0],s[4][1], line=s[1].line)]+s[8],
            lambda h,s: (s[2].lex,[]),
            lambda h,s: (s[2].lex,s[4]),
            lambda h,s: (None,[]),
            lambda h,s: ([s[1]]+s[2][0],s[2][1]),
            lambda h,s: (s[2][0],[s[1]]+s[2][1]),
            lambda h,s: ([],[]),
            lambda h,s: AttributeNode(IdentifierNode(s[1].lex,None,s[2],line=s[1].line),s[4],s[2],line=s[1].line),
            lambda h,s: MethodNode(s[1].lex, s[6], s[3], s[5], line=s[1].line),
            
            # Lista de parámetros opcionalmente tipados
            lambda h,s:[],
            lambda h,s:s[2],
            lambda h,s:[(s[1].lex,s[2])],
            lambda h,s:[(s[1].lex,s[2])] + s[4],
            lambda h,s:[],
            
            # Tipado opcional
            lambda h, s: s[2].lex,
            lambda h, s: None,
            
            # Lista de parametros con tipado obligatorio
            lambda h,s:[],
            lambda h,s:[(s[1].lex,s[3].lex)],
            lambda h,s:[(s[1].lex,s[3].lex)] + s[5],
            
            # Lista de variables
            lambda h, s: [s[1]],
            lambda h, s: [s[1]] + s[3],
            
            # Lista de expresiones
            lambda h, s: [s[1]],
            lambda h, s: [s[1]] + s[3],
            
            # Bloques especiales
            lambda h, s: s[1],
            lambda h, s: s[1],
            lambda h, s: BlockNode(s[2], line = s[1].line),
            
            # Lista de bloques especiales
            lambda h, s: [s[1]],
            lambda h, s: [s[1]] + s[2],
            
            # Expresiones
            lambda h, s: s[1],
            lambda h, s: MultipleLet(s),
            lambda h, s: IfNode(s[3], s[5], s[8], s[6][0], s[6][1], line=s[1].line),
            lambda h, s: IfNode(s[3], s[5], s[9], s[7][0], s[7][1], line=s[1].line),
            lambda h, s: WhileNode(s[3], s[5], line=s[1].line),
            lambda h, s: ForRangeToWhile(s),
            lambda h, s: ForToWhile(s),
            lambda h, s: PrintNode(s[3], line=s[1].line),
            lambda h, s: DestructNode(s[1], s[3], line=s[2].line),
            lambda h, s: ObjectCreationNode(s[2].lex, s[4], line=s[1].line),
            lambda h, s: ObjectCreationNode(s[2].lex, [], line=s[1].line),
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
            lambda h, s: AssignNode(s[1], s[4], s[2], line=s[3].line),
            
            
            # Expresion calculable
            lambda h,s:s[1],
            
            # Expresiones de cadena
            lambda h,s:ConcatSpaceNode(s[1],s[3], line=s[2].line),
            lambda h,s:ConcatSpaceNode(s[1],NumberNode(s[3].lex), line=s[2].line),
            lambda h,s:ConcatSpaceNode(s[1],StringNode(s[3].lex), line=s[2].line),
            lambda h,s:ConcatSpaceNode(s[1],s[3], line=s[2].line),
            lambda h,s:ConcatNode(s[1],s[3], line=s[2].line),
            lambda h,s:ConcatNode(s[1],NumberNode(s[3].lex), line=s[2].line),
            lambda h,s:ConcatNode(s[1],StringNode(s[3].lex), line=s[2].line),
            lambda h,s:ConcatNode(s[1],s[3], line=s[2].line),
            lambda h,s:s[1],
            
            # Expresiones logicas
            lambda h,s:OrNode(s[1],s[3], line=s[2].line),
            lambda h,s:OrNode(s[1],s[3], line=s[2].line),
            lambda h,s:s[1],
            
            lambda h, s: AndNode(s[1], s[3], line=s[2].line),
            lambda h, s: AndNode(s[1], s[3], line=s[2].line),
            lambda h,s:s[1],
            
            lambda h, s: NotNode(s[2], line=s[1].line),
            lambda h, s: IsNode(s[1], s[3].lex, line=s[2].line),
            lambda h, s: s[1],
            
            # Expresiones comparativas
            lambda h, s: EQNode(s[1], s[3], line=s[2].line),
            lambda h, s: NENode(s[1], s[3], line=s[2].line),
            lambda h, s: GENode(s[1], s[3], line=s[2].line),
            lambda h, s: GTNode(s[1], s[3], line=s[2].line),
            lambda h, s: LENode(s[1], s[3], line=s[2].line),
            lambda h, s: LTNode(s[1], s[3], line=s[2].line),
            lambda h, s: s[1],
            
            # Expresiones aritmeticas
            lambda h, s: PlusNode(s[1], s[3], line=s[2].line),
            lambda h, s: MinusNode(s[1], s[3], line=s[2].line),
            lambda h, s: s[1],
            
            lambda h, s: StarNode(s[1], s[3], line=s[2].line),
            lambda h, s: DivNode(s[1], s[3], line=s[2].line),
            lambda h, s: ModNode(s[1], s[3], line=s[2].line),
            lambda h, s: s[1],
            
            lambda h, s: PowNode(s[1], s[3], line=s[2].line),
            lambda h, s: PowNode(s[1], s[3], line=s[2].line),
            lambda h, s: SinNode(s[3], line=s[1].line),
            lambda h, s: CosNode(s[3], line=s[1].line),
            lambda h, s: SqrtNode(s[3], line=s[1].line),
            lambda h, s: ExpNode(s[3], line=s[1].line),
            lambda h, s: LogNode(s[3], s[5], line=s[1].line),
            lambda h, s: RandNode(line=s[1].line),
            lambda h, s: s[1],
            
            lambda h, s: NumberNode(s[1].lex, line=s[1].line),
            lambda h, s: NumberNode(s[1].lex, line=s[1].line),
            lambda h, s: NumberNode(s[1].lex, line=s[1].line),
            lambda h, s: BoolNode(s[1].lex, line=s[1].line),
            lambda h, s: BoolNode(s[1].lex, line=s[1].line),
            lambda h, s: StringNode(s[1].lex, line=s[1].line),
            lambda h, s: s[2],
            # lambda h, s: s[1],
            lambda h, s: VectorNode(s[2], line=s[1].line),
            lambda h, s: VectorImplicitNode(s[2],s[4],s[8],s[10], line=s[1].line),
            lambda h, s: CallNode(s[1],[s[3],s[5]], line=s[2].line),
            lambda h, s: s[1],
            lambda h, s: VectorIndex(s[1].lex,s[3], line=s[2].line),
            lambda h, s: AsNode(s[1],s[3].lex, line=s[2].line),
            lambda h, s: s[1],

            # Expresiones self
            # lambda h, s: SelfNode(s[3]),
            # lambda h, s: SelfNode(IdentifierNode(s[3],s[5])),
            # lambda h, s: SelfNode(s[3]),
            
            # Objetos recurrentes
            lambda h, s: CallNode(s[1].lex, s[3], s[6], line=s[2].line),
            lambda h, s: CallNode(s[1].lex, [], s[5], line=s[2].line),
            lambda h, s: CallNode(s[1].lex, s[3], line=s[2].line),
            lambda h, s: CallNode(s[1].lex, line=s[2].line),
            
            # Identificador
            lambda h, s: IdentifierNode(s[1].lex, line=s[1].line),
            lambda h, s: IdentifierNode(s[1].lex, s[3], line=s[1].line),
            lambda h, s: IdentifierNode(s[1].lex, IdentifierNode(s[3], s[5]), line=s[1].line),
            lambda h, s: IdentifierNode(s[1].lex, s[3], line=s[1].line)
            
        ]

        program %= stats + specialBlock + stats
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
        expr %= ifx + opar + expr + cpar + expr + elifx_expr + elsex + superexpr
        expr %= ifx + opar + expr + cpar + expr + semicolon + elifx_expr + elsex + superexpr
        expr %= whilex + opar + expr + cpar + expr
        expr %= forx + opar + idnode + inx + rangex + opar + expr + comma + expr + cpar + cpar + expr
        expr %= forx + opar + idnode + inx + idnode + cpar + expr
        expr %= printx + opar + expr + cpar
        expr %= idnode + asign2 + expr
        expr %= new + idx + opar + arg_expr + cpar
        expr %= new + idx + opar + cpar
        expr %= calc_expr

        # Super expresion
        superexpr %= expr
        superexpr %= obrace + cbrace

        # Cuerpo del elif
        elifx_expr %= elifx + opar + expr + cpar + expr + elifx_expr
        elifx_expr %= self.G.Epsilon

        # Lista de asignaciones para el let
        asig_list %= asig1
        asig_list %= asig1 + comma + asig_list
        asig1 %= idnode + opt_typed + asign1 + expr




        # Expresion calculable
        calc_expr %= string_expr
        
        # Expresiones de cadena
        string_expr %= string_expr + concat_space + idnode
        string_expr %= string_expr + concat_space + number
        string_expr %= string_expr + concat_space + string
        string_expr %= string_expr + concat_space + recurrent_object
        string_expr %= string_expr + concat + idnode
        string_expr %= string_expr + concat + number
        string_expr %= string_expr + concat + string
        string_expr %= string_expr + concat + recurrent_object
        string_expr %= logical_expr

        # Expresiones lógicas
        logical_expr %= logical_expr + orx + logical_term
        logical_expr %= logical_expr + orx2 + logical_term
        logical_expr %= logical_term
        
        logical_term %= logical_term + andx + logical_factor
        logical_term %= logical_term + andx2 + logical_factor
        logical_term %= logical_factor
        
        logical_factor %= notx + logical_factor
        logical_factor %= idnode + isx + idx
        logical_factor %= comparative_expr
        
        # Expresiones comparativas 
        comparative_expr %= aritmetic_expr + eq + aritmetic_expr
        comparative_expr %= aritmetic_expr + ne + aritmetic_expr
        comparative_expr %= aritmetic_expr + ge + aritmetic_expr
        comparative_expr %= aritmetic_expr + gt + aritmetic_expr
        comparative_expr %= aritmetic_expr + le + aritmetic_expr
        comparative_expr %= aritmetic_expr + lt + aritmetic_expr
        comparative_expr %= aritmetic_expr
        
        # Expresiones aritmeticas
        aritmetic_expr %= aritmetic_expr + plus + aritmetic_term
        aritmetic_expr %= aritmetic_expr + minus + aritmetic_term
        aritmetic_expr %= aritmetic_term

        aritmetic_term %= aritmetic_term + star + aritmetic_factor
        aritmetic_term %= aritmetic_term + div + aritmetic_factor
        aritmetic_term %= aritmetic_term + mod + aritmetic_factor
        aritmetic_term %= aritmetic_factor

        aritmetic_factor %= aritmetic_factor + powx + aritmetic_atom
        aritmetic_factor %= aritmetic_factor + star2 + aritmetic_atom
        aritmetic_factor %= sin + opar + aritmetic_expr + cpar
        aritmetic_factor %= cos + opar + aritmetic_expr + cpar
        aritmetic_factor %= sqrt + opar + aritmetic_expr + cpar
        aritmetic_factor %= exp + opar + aritmetic_expr + cpar
        aritmetic_factor %= log + opar + aritmetic_expr + comma + aritmetic_expr + cpar
        aritmetic_factor %= rand + opar + cpar
        aritmetic_factor %= aritmetic_atom

        aritmetic_atom %= number
        aritmetic_atom %= pi
        aritmetic_atom %= e
        aritmetic_atom %= true
        aritmetic_atom %= false
        aritmetic_atom %= string
        aritmetic_atom %= opar + expr + cpar
        # aritmetic_atom %= self_expr
        aritmetic_atom %= obrake + arg_expr + cbrake
        aritmetic_atom %= obrake + calc_expr + implicit + idnode + inx + rangex + opar + calc_expr + comma + calc_expr + cpar + cbrake
        aritmetic_atom %= rangex + opar + expr + comma + expr + cpar
        aritmetic_atom %= idnode
        aritmetic_atom %= idx + obrake + calc_expr + cbrake
        aritmetic_atom %= idnode + asx + idx
        aritmetic_atom %= recurrent_object

        # Expresiones self
        # self_expr %= selfx + dot + idnode
        # self_expr %= selfx + dot + idx + dot + recurrent_object
        # self_expr %= selfx + dot + recurrent_object

        # Expresiones recurrentes
        recurrent_object %= idx + opar + arg_expr + cpar + dot + recurrent_object
        recurrent_object %= idx + opar + cpar + dot + recurrent_object
        recurrent_object %= idx + opar + arg_expr + cpar
        recurrent_object %= idx + opar + cpar

        # Identificador
        idnode %= idx
        idnode %= idx + dot + idnode
        idnode %= idx + dot + idx + recurrent_object
        idnode %= idx + dot + recurrent_object

        #############################################################################

        lexer = Lexer('eof', self.terminals)
        if lexer.errors:
            self.error_msg = '\n'.join(lexer.errors)
            self.ast = None
            return
        
        tokens = lexer(text)

        ###################################################################################

        parser = LR1Parser(self.G, 'parser')

        derivations,msg = parser(tokens)
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
            {
                let a = 10 in while (a >= 0) {
                    print(a);
                    a := a - 1;
                };
                
                for (x in range(0, 10)) print(x);
                let iterable = range(0, 10) in
                    while (iterable.next())
                        let x = iterable.current() in
                            print(x);
            }
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
