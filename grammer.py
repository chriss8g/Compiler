from cmp.pycompiler import Grammar
from my_types import *

class CodeToAST:
    
    def __init__(self, text):
        self.G = Grammar()

        # Definir los no terminales
        program = self.G.NonTerminal('<program>', startSymbol=True)
        stat_list, stat = self.G.NonTerminals('<stat_list> <stat>')
        expr, term, factor, atom = self.G.NonTerminals('<expr> <term> <factor> <atom>')
        arg_list, func_call, expr_list, asig_list = self.G.NonTerminals('<arg_list> <func_call> <expr_list> <asig_list>')

        # Definir los terminales
        let, functionx, inx = self.G.Terminals('let function in')
        printx, sin, cos, sqrt, exp, log, rand = self.G.Terminals('print sin cos sqrt exp log rand')
        semi, comma, opar, cpar, arrow = self.G.Terminals('; , ( ) =>')
        asign, plus, minus, star, div = self.G.Terminals('= + - * /')
        pow, mod, andx, orx, notx = self.G.Terminals('^ % & | !')
        eq, gt, lt, ge, le = self.G.Terminals('== > < >= <=')
        ne, concat, lbrace, rbrace, asign2 = self.G.Terminals('!= @ { } :=')
        pi, e, true, false = self.G.Terminals('PI E true false')
        idx, number, string = self.G.Terminals('id num string')
        ifx, elsex, elifx, whilex, forx, range = self.G.Terminals('if else elif while for range')

        # Definir las producciones y sus acciones
        program %= stat_list, lambda h, s: ProgramNode(s[1])

        stat_list %= stat + semi, lambda h, s: [s[1]]
        stat_list %= stat + semi + stat_list, lambda h, s: [s[1]] + s[3]

        stat %= let + asig_list + inx + expr, lambda h, s: VarDeclarationNode(s[2][0], s[2][1], s[4])
        stat %= functionx + idx + opar + arg_list + cpar + arrow + expr, lambda h, s: FuncDeclarationNode(s[2], s[4], s[7])
        stat %= printx + expr, lambda h, s: PrintNode(s[2])
        stat %= whilex + opar + expr + cpar + stat, lambda h, s: WhileNode(s[3], s[5])
        stat %= forx + opar + idx + inx + expr + cpar + stat, lambda h, s: ForNode(s[3], s[5], s[7])
        stat %= ifx + opar + expr + cpar + stat + elsex + stat, lambda h, s: IfNode(s[3], s[5], s[7], [], [])
        stat %= ifx + opar + expr + cpar + stat + elifx + opar + expr + cpar + stat + elsex + stat, lambda h, s: IfNode(s[3], s[5], s[11], [s[8]], [s[10]])

        arg_list %= idx, lambda h, s: [s[1]]
        arg_list %= idx + comma + arg_list, lambda h, s: [s[1]] + s[3]

        expr %= expr + plus + term, lambda h, s: PlusNode(s[1], s[3])
        expr %= expr + minus + term, lambda h, s: MinusNode(s[1], s[3])
        expr %= term, lambda h, s: s[1]

        term %= term + star + factor, lambda h, s: StarNode(s[1], s[3])
        term %= term + div + factor, lambda h, s: DivNode(s[1], s[3])
        term %= term + pow + factor, lambda h, s: PowNode(s[1], s[3])
        term %= factor, lambda h, s: s[1]

        factor %= opar + expr + cpar, lambda h, s: s[2]
        factor %= number, lambda h, s: ConstantNumNode(s[1])
        factor %= true, lambda h, s: BoolNode(s[1])
        factor %= false, lambda h, s: BoolNode(s[1])
        factor %= pi, lambda h, s: ConstantNumNode(s[1])
        factor %= e, lambda h, s: ConstantNumNode(s[1])
        factor %= string, lambda h, s: StringNode(s[1])
        factor %= idx, lambda h, s: VariableNode(s[1])
        factor %= func_call, lambda h, s: s[1]

        func_call %= idx + opar + expr_list + cpar, lambda h, s: CallNode(s[1], s[3])

        expr_list %= expr, lambda h, s: [s[1]]
        expr_list %= expr + comma + expr_list, lambda h, s: [s[1]] + s[3]

        asig_list %= idx + asign + expr, lambda h, s: [[s[1]], [s[3]]]
        asig_list %= idx + asign + expr + comma + asig_list, lambda h, s: [[s[1]] + s[5][0], [s[3]] + s[5][1]]

        #############################################################################


        from cmp.utils import Token, tokenizer

        fixed_tokens = { t.Name: Token(t.Name, t) for t in self.G.terminals if t not in { idx, number }}

        @tokenizer(self.G, fixed_tokens)
        def tokenize_text(token):
            lex = token.lex
            try:
                float(lex)
                return token.transform_to(number)
            except ValueError:
                    return token.transform_to(idx)

        tokens = tokenize_text(text)


        ###################################################################################


        from cmp.tools.parsing import LR1Parser

        parser = LR1Parser(self.G)


        parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)
        # print('\n'.join(repr(x) for x in parse))


        from cmp.evaluation import evaluate_reverse_parse

        self.ast = evaluate_reverse_parse(parse, operations, tokens)
        

    def __repr__(self):
        from FormatVisitor import FormatVisitor

        formatter = FormatVisitor()
        tree = formatter.visit(self.ast)
        return tree
    

if __name__ == "__main__":
      
      text ='''
                print 1 - 1 - 1 ;
                let x = 58 in x + 1 ;
                function f ( a , b ) => 5 + 6 ;
                print F ( 5 + x , 7 + y ) ;
            '''
      codeToAST = CodeToAST(text)
      print(codeToAST)
