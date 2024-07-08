from lexer.tokenizer import *
from utils.pycompiler import Grammar


nonzero_digits = '|'.join(str(n) for n in range(1,10))
lettersLowerCase = '|'.join(chr(n) for n in range(ord('a'),ord('z')+1))
lettersUpperCase = '|'.join(chr(n) for n in range(ord('A'),ord('Z')+1))

# Expresiones regulares
regular_expresions = [
    ('function', 'function'),
    ('inherits', 'inherits'),
    ('type', 'type'),
    ('return', 'return'),
    ('new', 'new'),
    ('self', 'self'),
    ('dot', '.'),
    ('sin', 'sin'),
    ('cos', 'cos'),
    ('sqrt', 'sqrt'),
    ('exp', 'exp'),
    ('log', 'log'),
    ('rand', 'rand'),
    ('print', 'print'),
    ('PI', 'PI'),
    ('E', 'E'),
    ('let', 'let'),
    ('in', 'in'),
    ('true', 'true'),
    ('false', 'false'),
    ('if', 'if'), 
    ('else', 'else'),
    ('elif', 'elif'),
    ('while', 'while'),
    ('for', 'for'),
    ('range', 'range'),
    ('num', f'0|({nonzero_digits})(0|{nonzero_digits})*'),
    ('id', f'({lettersLowerCase}|{lettersUpperCase}|_)({lettersLowerCase}|{lettersUpperCase}|_|0|{nonzero_digits})*'),
    ('string', f'"({lettersLowerCase}|{lettersUpperCase}|0|{nonzero_digits}|@|##|#||=|:|,|#(|#)|+|-|#*|/|^|%|#$| |\\"|!|<|>|\\|@|;|[|])*"'),
    ('asign1','='),
    ('asign2',':='),
    ('comma', ','),
    ('opar', '#('),
    ('cpar', '#)'),
    ('plus', '+'),
    ('minus', '-'),
    ('star','#*'),
    ('divide', '/'),
    ('pow', '^'),
    ('mod', '%'),
    ('and', '&'),
    ('or', '#|'),
    ('not', '!'),
    ('eq', '=='),
    ('ne', '!='),
    ('gt', '>'),
    ('ge', '>='),
    ('lt', '<'),
    ('le', '<='),
    ('concat', '@'),
    ('concat_space', '@@'),
    ('lbrace', '{'),
    ('rbrace', '}'),
    ('lbrake', '['),
    ('rbrake', ']'),
    ('semi', ';'),
    ('colon', ':'),
    ('arrow', '=>')
]

class Lexer:
    def __init__(self, eof, terminals):
        global regular_expresions
        
        self.eof = eof
        self.regexs = self._build_regexs(regular_expresions)
        self.errors = []
        self.terminals = terminals
    
    def _build_regexs(self, table):
        automatonMaker = RegexHandler()
        regexs = []
        for _, (tag, regex) in enumerate(table):
            autom = automatonMaker(regex)
            regexs.append({
                "tag": tag,
                "autom":autom,
                "active":True,
                "state":[0],
                "count":0
            })
        return regexs
    
    def _reset_automs(self):
        
        for regex in self.regexs:
            regex['active'] = True
            regex['count'] = 0
            regex['state'] = {0}
    
    def _getAceptedTag(self, regexs):
        max = 0
        accepted_regex = None

        for r in regexs:
            if r['count'] > max and r['state'].issubset(r['autom'].finals):
                
                max = r['count']
                accepted_regex = r
        
        if max == 0:
            return None

        last_state = accepted_regex['state']
        autom = accepted_regex['autom']

        if last_state.issubset(autom.finals):
            return accepted_regex['tag']
        else:
            return None
        
    def _walk(self, text):
        
        head = 0
        
        for c in text:
            head += 1 

            for regex in self.regexs:
                if not regex['active']:
                    continue

                state = regex['state']
                new_state = move(regex['autom'],state,c)
                
                if new_state == set():
                    regex['active'] = False
                    continue

                regex['count'] += 1
                regex['state'] = new_state
            
            accepted = False
            for r in self.regexs:
                accepted = accepted or r['active']
            
            if not accepted:
                head -= 1
                break
                
        tag = None
        
        if head > 0:
            tag = self._getAceptedTag(self.regexs)
        else:
            head = 1

        lex = text[:head]
        
        return lex,tag
    
    def _tokenize(self, text):
        
        while text:
            text = text.lstrip()
            self._reset_automs()
            
            lex,tag = self._walk(text)
            text = text[len(lex):]
            
            if tag is None:
                self.errors.append(f'Caracter {lex} desconocido')
                continue
            yield lex,tag
            
        yield '$', self.eof
    
    def __call__(self, text):
        return [ Token(lex, self.terminals[ttype]) for lex, ttype in self._tokenize(text) ]
    

    
    
    
    


if __name__ == "__main__":

    nonzero_digits = '|'.join(str(n) for n in range(1,10))
    lettersUpperCase = '|'.join(chr(n) for n in range(ord('A'),ord('Z')+1))

    # print('Non-zero digits:', nonzero_digits)
    # print('Letters:', lettersUpperCase)


    # lexer = Lexer('eof')

    # text = '''print("a b")'''
    # print(f'\n>>> Tokenizando: "{text}"')
    # tokens = lexer(text)
    
    # if lexer.errors:
    #     for e in lexer.errors:
    #         print(e)
    
    # print('\n',tokens)

    autom_maker = RegexHandler()
    
    autom = autom_maker('"(##|a)*"')
    
    dfa = nfa_to_dfa(autom)
    
    print(dfa.recognize('"#"'))