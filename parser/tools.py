import os
import pickle
from utils.pycompiler import Item
from utils.automate import State, multiline_formatter
from utils.utils import ContainerSet

def compute_local_first(firsts, alpha):
    first_alpha = ContainerSet()
    
    try:
        alpha_is_epsilon = alpha.IsEpsilon
    except:
        alpha_is_epsilon = False
    
    if(alpha_is_epsilon):
        first_alpha.set_epsilon(True)
        return first_alpha
    
    for symbol in alpha:
        first_symbol = firsts[symbol]
        first_alpha.update(first_symbol)
        if(not first_symbol.contains_epsilon):
            break
            
    return first_alpha

def compute_firsts(G):
    firsts = {}
    change = True
    
    for terminal in G.terminals:
        firsts[terminal] = ContainerSet(terminal)
    
    for nonterminal in G.nonTerminals:
        firsts[nonterminal] = ContainerSet()
    
    while change:
        change = False
        
        for production in G.Productions:
            X = production.Left
            alpha = production.Right
            
            first_X = firsts[X]
                
            try:
                first_alpha = firsts[alpha]
            except KeyError:
                first_alpha = firsts[alpha] = ContainerSet()
            
            local_first = compute_local_first(firsts, alpha)
            
            change |= first_alpha.hard_update(local_first)
            change |= first_X.hard_update(local_first)
                    
    return firsts


def expand(item: Item, firsts):
    next_symbol = item.NextSymbol
    if next_symbol is None or not next_symbol.IsNonTerminal:
        return []
    
    lookaheads = ContainerSet()

    for x in item.Preview():
        lookaheads.update(compute_local_first(firsts, x))
        
    productions = next_symbol.productions
    
    return [Item(production, 0, lookaheads) for production in productions]
    
def compress(items):
    centers = {}

    for item in items:
        center = item.Center()
        try:
            lookaheads = centers[center]
        except KeyError:
            centers[center] = lookaheads = set()
        lookaheads.update(item.lookaheads)
    
    return { Item(x.production, x.pos, set(lookahead)) for x, lookahead in centers.items() }


def closure_lr1(items, firsts):
    closure = ContainerSet(*items)
    
    changed = True
    while changed:
        changed = False
        
        new_items = ContainerSet()
        
        for x in closure:
            expanded=expand(x, firsts)
            new_items.update(ContainerSet(*expanded))
                    
        changed = closure.update(new_items)
        
    return compress(closure)
   
def goto_lr1(items, symbol, firsts=None, just_kernel=False):
    assert just_kernel or firsts is not None, '`firsts` must be provided if `just_kernel=False`'
    items = frozenset(item.NextItem() for item in items if item.NextSymbol == symbol)
    return items if just_kernel else closure_lr1(items, firsts)

def build_LR1_automaton(G):
    
    firsts = compute_firsts(G)
    firsts[G.EOF] = ContainerSet(G.EOF)
    
    start_production = G.startSymbol.productions[0]
    start_item = Item(start_production, 0, lookaheads=(G.EOF,))
    start = frozenset([start_item])
    
    closure = closure_lr1(start, firsts)

    automaton = State(frozenset(closure), True)

    pending = [ start ]
    visited = { start: automaton }

    while pending:
        current = pending.pop()
        
        current_state = visited[current]
          
        new_closure = closure_lr1(current_state.state, firsts)
        for new_item in new_closure:
            for symbol in G.terminals + G.nonTerminals:
                next_state = None
                if symbol.Name in current_state.transitions:
                    continue
                if new_item.NextSymbol == symbol:

                    next_state = goto_lr1(new_closure, symbol, firsts=firsts)
                    
                    if next_state:
                        frozen = frozenset(next_state)

                        if not frozen in visited:

                            pending.append(frozen)
                            new_state = State(frozen, True)
                            visited[frozen] = new_state
                            current_state.add_transition(symbol.Name, new_state)
                        else:
                            current_state.add_transition(symbol.Name, visited[frozen])
                    
    automaton.set_formatter(multiline_formatter)
    return automaton


class ShiftReduceParser:

    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'
    OK = 'OK'

    def __init__(self, G, parser_name ,verbose=False):
        self.G = G
        self.verbose = verbose
        self.action = {}
        self.goto = {}
        
        if parser_name == "parser":
            if os.path.exists('./parser/action'):
                with open('./parser/action', 'rb') as file1:
                    self.action = pickle.load(file1)
                with open('./parser/goto', 'rb') as file2:
                    self.goto = pickle.load(file2)
            else:
                self._build_parsing_table(parser_name)   
        else:
            self._build_parsing_table()

    def _build_parsing_table(self):
        raise NotImplementedError()

    def __call__(self, w, get_shift_reduce=False):
        stack = [0]
        cursor = 0
        output = []
        operations = []
        while True:
            state = stack[-1]
            lookahead = w[cursor]

            if(state, lookahead) not in self.action:
                excepted_char = ''

                for (state1, i) in self.action:
                    if i.IsTerminal and state1 == state:
                        excepted_char += str(i) + ', '
                parsed = ' '.join([str(m)
                                    for m in stack if not str(m).isnumeric()])
                excepted_char = excepted_char.rstrip(', ')
                message_error = f'It was expected "{excepted_char}" received "{lookahead}" after {parsed}'
                # print("\nError. Aborting...")
                # print('')
                # print("\n", message_error)

                return None,message_error

            if self.action[state, lookahead] == self.OK:
                action = self.OK
            else:
                action, tag = self.action[state, lookahead]

            if action == self.SHIFT:
                operations.append(self.SHIFT)
                stack += [lookahead, tag]
                cursor += 1
            elif action == self.REDUCE:
                operations.append(self.REDUCE)
                output.append(tag)

                head, body = tag
                for symbol in reversed(body):
                    stack.pop()

                    assert stack.pop() == symbol
                    state = stack[-1]

                goto = self.goto[state, head]
                stack += [head, goto]
            elif action == self.OK:
                stack.pop()
                assert stack.pop() == self.G.startSymbol
                assert len(stack) == 1
                return output,'Clean Code' if not get_shift_reduce else(output, 'Operations: ' + ', '.join(op for op in operations))
            else:
                return None,'Invalid Code'

class LR1Parser(ShiftReduceParser):
    def __init__(self, G, parser_name='lexer' ,verbose=False):
        super().__init__(G, parser_name, verbose)
    
    def _build_parsing_table(self, parser_name='lexer'):
        G = self.G.AugmentedGrammar(True)
        
        automaton = build_LR1_automaton(G)
        
        for i, node in enumerate(automaton):
            if self.verbose: print(i, '\t', '\n\t '.join(str(x) for x in node.state), '\n')
            node.idx = i
        
        for node in automaton:
            idx = node.idx
            for item in node.state:
                    
                if  item.NextSymbol and item.NextSymbol.IsTerminal:
                    self._register(self.action, (idx, item.NextSymbol), (self.SHIFT,node.get(item.NextSymbol.Name).idx))
                elif not item.NextSymbol and not item.production.Left == G.startSymbol:
                    
                    for lookahead in item.lookaheads:
                        self._register(self.action, (idx, lookahead), (self.REDUCE, item.production))
                
                elif item.IsReduceItem and item.production.Left == G.startSymbol and not item.NextSymbol:
                    
                    self._register(self.action, (idx, G.EOF), self.OK)

                else:
                    self._register(self.goto, (idx, item.NextSymbol), node.get(item.NextSymbol.Name).idx)
        
        if parser_name == "parser":
            with open('./parser/action', 'wb') as file1:
                pickle.dump(self.action, file1)
            with open('./parser/goto', 'wb') as file2:
                pickle.dump(self.goto, file2)
        
    @staticmethod
    def _register(table, key, value):
        assert key not in table or table[key] == value, 'Shift-Reduce or Reduce-Reduce conflict!!!'
        table[key] = value
     
       
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
    
    def __init__(self, lex, token_type):
        self.lex = lex
        self.token_type = token_type
    
    def __str__(self):
        return f'{self.token_type}: {self.lex}'
    
    def __repr__(self):
        return str(self)
    
# *******************************************
# ********** Atributar Gramatica ************
# *******************************************


def evaluate_parse(left_parse, tokens, G=None, attributes=None):
    
    if G:
        for i in range(len(G.Productions)):
            G.attributes[G.Productions[i]] = attributes[i]
    
    if not left_parse or not tokens:
        return
    
    left_parse = iter(left_parse)
    tokens = iter(tokens)
    next(tokens)
    result = evaluate(next(left_parse), left_parse, tokens, G)
    
    return result
    
def evaluate(production, left_parse, tokens, G, inherited_value=None):
    _, body = production
    
    attributes = None
    if not G:
        attributes = production.attributes
    else:
        attribute = G.attributes[production]
        attributes = [None for i in range(len(body)+1)]
        attributes[0] = attribute
        
    
    synteticed = []
    inherited = []
    for i in range(len(attributes)):
        synteticed.append(None)
        inherited.append(None)
    
    inherited[0] = inherited_value
    
    for i, symbol in enumerate(reversed(body),1):
        index = len(body)-i
        if symbol.IsTerminal:
            a = next(tokens).lex
            synteticed[index+1] = a
        else:
            next_production = next(left_parse)
            synteticed[index+1] = evaluate(next_production,left_parse,tokens,G, inherited_value)

    return attributes[0](inherited, synteticed)
    
