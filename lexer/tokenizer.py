from utils.pycompiler import Grammar
from lexer.Nodes import *
from lexer.parser_tools import *


class Token:
    """
    Basic token class.

    Parameters
    ----------
    lex : str
        Token's lexeme.
    token_type : Enum
        Token's type.
    """

    def __init__(self, lex, token_type, line=0):
        self.lex = lex
        self.token_type = token_type
        self.line = line

    def __str__(self):
        return f'{self.token_type}: {self.lex}, in [line:{self.line}]'

    def __repr__(self):
        return str(self)

    @property
    def is_valid(self):
        return True

class UnknownToken(Token):
    def __init__(self, lex):
        Token.__init__(self, lex, None)

    def transform_to(self, token_type):
        return Token(self.lex, token_type)

    @property
    def is_valid(self):
        return False



class RegexHandler:
    def __init__(self):
        self.grammar = self._build_grammar()
    
    def _build_grammar(self):
        G = Grammar()
        E = G.NonTerminal('E', True)
        T, F = G.NonTerminals('T F')
        self.pipe, self.star, self.opar, self.cpar, self.symbol = G.Terminals('| * ( ) symbol')

        # > PRODUCTIONS??? LR(1) Grammar
        E %= E + self.pipe + T, lambda h,s: UnionNode(s[1],s[3])
        E %= T, lambda h,s: s[1]

        T %= T + F, lambda h,s: ConcatNode(s[1],s[2])
        T %= F, lambda h,s: s[1]

        F %= self.opar + E + self.cpar, lambda h,s: s[2]
        F %= F + self.star, lambda h,s: ClosureNode(s[1])
        F %= self.symbol, lambda h,s: SymbolNode(s[1])

        return G

    def _regex_tokenizer(self, text, skip_whitespaces=False):
        tokens = []
        tmp = ''
        text = text + '$'
        
        ignore_char = False

        for char in text:
            if skip_whitespaces and char.isspace():
                continue
            
            if ignore_char:
                ignore_char = False
                tokens.append(Token(char,self.symbol))
                continue
            if char == '#':
                ignore_char = True
                continue
            
            if char == '|':
                tokens.append(Token(char,self.pipe))
            elif char == '*':
                tokens.append(Token(char,self.star))
            elif char == '(':
                tokens.append(Token(char,self.opar))
            elif char == ')':
                tokens.append(Token(char,self.cpar))
            elif char == '$':
                tokens.append(Token('$', self.grammar.EOF))
                break
            else:
                tokens.append(Token(char,self.symbol))
            
        return tokens

    def _build_automaton(self, text):

        # Obtener los tokens de la expresion regular
        tokens = self._regex_tokenizer(text)
        
        parser = LR1Parser(self.grammar)
        derivations,_ = parser(tokens)
        
        tokens.reverse()
        derivations.reverse()

        result = evaluate_parse(derivations, tokens)

        nfa = result.evaluate()

        dfa = nfa_to_dfa(nfa)

        return dfa

    def __call__(self,text):
        return self._build_automaton(text)


