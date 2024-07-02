from lexer.pycompiler import Production, Sentence, Symbol, EOF, Epsilon



class NFA:
    def __init__(self, states, finals, transitions, start=0):
        self.states = states
        self.start = start
        self.finals = set(finals)
        self.map = transitions
        self.vocabulary = set()
        self.transitions = { state: {} for state in range(states) }
        
        for (origin, symbol), destinations in transitions.items():
            assert hasattr(destinations, '__iter__'), 'Invalid collection of states'
            self.transitions[origin][symbol] = destinations
            self.vocabulary.add(symbol)
            
        self.vocabulary.discard('')

    def __getitem__(self,symbol:str,state=0):
        try:
            return self.map[state,symbol]
        except:
            print('No hay transiciones desde ese estado con ese símbolo')
            return None

    def epsilon_transitions(self, state):
        assert state in self.transitions, 'Invalid state'
        try:
            return self.transitions[state]['']
        except KeyError:
            return ()
            
    # def graph(self):
    #     G = pydot.Dot(rankdir='LR', margin=0.1)
    #     G.add_node(pydot.Node('start', shape='plaintext', label='', width=0, height=0))

    #     for (start, tran), destinations in self.map.items():
    #         tran = 'ε' if tran == '' else tran
    #         G.add_node(pydot.Node(start, shape='circle', style='bold' if start in self.finals else ''))
    #         for end in destinations:
    #             G.add_node(pydot.Node(end, shape='circle', style='bold' if end in self.finals else ''))
    #             G.add_edge(pydot.Edge(start, end, label=tran, labeldistance=2))

    #     G.add_edge(pydot.Edge('start', self.start, label='', style='dashed'))
    #     return G

    def _repr_svg_(self):
        try:
            return self.graph().create_svg().decode('utf8')
        except:
            pass

class DFA(NFA):
    
    def __init__(self, states, finals, transitions, start=0):
        assert all(isinstance(value, int) for value in transitions.values())
        assert all(len(symbol) > 0 for origin, symbol in transitions)
        
        transitions = { key: [value] for key, value in transitions.items() }
        NFA.__init__(self, states, finals, transitions, start)
        self.current = start
        
    def _move(self, symbol):
        if self.current in self.transitions:
            if symbol in self.transitions[self.current]:
                return self.transitions[self.current][symbol][0]
        return None
        
    
    def _reset(self):
        self.current = self.start
        
    def recognize(self, string):
        self._reset()
        for symbol in string:
            self.current = self._move(symbol)
        return self.current in self.finals
    
    
def move(automaton, states, symbol):
    moves = set()
    for state in states:
        if (not symbol in automaton.transitions[state]):
            continue  
        for i in automaton.transitions[state][symbol]:
            moves.add(i)  
    return moves
    
def epsilon_closure(automaton, states):
    pending = [ s for s in states ] # equivalente a list(states) pero me gusta así :p
    closure = { s for s in states } # equivalente a  set(states) pero me gusta así :p
    
    while pending:
        state = pending.pop()
        if (state,'') in automaton.map:
            for x in automaton.map[(state,'')]:
                closure.add(x)
                pending.append(x)
                
    return ContainerSet(*closure)

def nfa_to_dfa(automaton: NFA):
    transitions = {}
    
    start = epsilon_closure(automaton, [automaton.start])
    start.id = 0
    start.is_final = any(s in automaton.finals for s in start)
    states = [ start ]
    pending = [ start ]
    current_id = 1
    while pending:
        state = pending.pop()
        for symbol in automaton.vocabulary:
            # Your code here
            nfa_transitions_set = set()
                
            try:
                transitions[state.id, symbol]
                assert False, 'Invalid DFA!!!'
            except KeyError:
                # Your code here
                moves = move(automaton, list(state), symbol)
                new_state = epsilon_closure(automaton, list(moves))
                
                if len(new_state) > 0:
                    if new_state != state:
                        viewed_status = None
                        try:
                            viewed_status = states.index(new_state)
                        except ValueError:
                            pass

                        if viewed_status is None:
                            new_state.id = len(states) 
                            new_state.is_final = any(s in automaton.finals for s in new_state)
                            pending = [new_state] + pending
                            states.append(new_state)
                        else:
                            new_state.id = states[viewed_status].id
                            
                        transitions[state.id, symbol] = new_state.id
                    else :
                        transitions[state.id, symbol] = state.id
        
    finals = [ state.id for state in states if state.is_final ]
    dfa = DFA(len(states), finals, transitions)
    return dfa



def automata_union(a1, a2):
    
    states = a1.states + a2.states + 1
    start = 0
    transitions = {}

    # Estados finales
    finals1 = {c+1 for c in a1.finals}
    finals2 = {c+a1.states+1 for c in a2.finals}
    finals = set.union(finals1,finals2)

    for (origin,symb),dests in a1.map.items():
        if (origin,symb) in transitions:
            for dest in dests:
                transitions[origin+1,symb].append(dest+1)
        else:
            transitions[origin+1,symb] = [dest+1 for dest in dests]

    for (origin,symb),dests in a2.map.items():
        new_origin = origin+a1.states+1
        if (new_origin,symb) in transitions:
            for dest in dests:
                transitions[new_origin,symb].append(dest+a1.states+1)
        else:
            transitions[new_origin,symb] = [dest+a1.states+1 for dest in dests]
    
    # Agregar las transiciones del primer estado a los estados iniciales de los automatas
    transitions[0,''] = [1]
    transitions[0,''].append(a1.states+1)

    return NFA(states, finals, transitions, start)

def automata_concatenation(a1:NFA, a2:NFA):
    
    states = a1.states + a2.states
    start = a1.start
    finals = {a1.states+c for c in a2.finals}
    transitions = {}

    for (origin,symb),dests in a1.map.items():
        if (origin,symb) in transitions:
            for dest in dests:
                transitions[origin,symb].append(dest)
        else:
            transitions[origin,symb] = [dest for dest in dests]
    
    
    for (origin,symb),dests in a2.map.items():
        new_origin = origin+a1.states
        if (new_origin,symb) in transitions:
            for dest in dests:
                transitions[new_origin,symb].append(dest+a1.states)
        else:
            transitions[new_origin,symb] = [dest+a1.states for dest in dests]
    
    for f in a1.finals:
        if (f,'') in transitions:
            transitions[f,''].append(a1.states)
        else:
            transitions[f,''] = [a1.states]
    
    return NFA(states, finals, transitions, start)

def automata_closure(a1:NFA):  # Funciona
    
    states = a1.states
    start = a1.start
    finals = a1.finals
    transitions = {}
    
    for (origin,symb),dests in a1.map.items():
        transitions[(origin,symb)] = [dest for dest in dests]
    
    for state in finals:
        transitions[state,''] = [start]

    finals.add(start)

    
    return NFA(states, finals, transitions, start)




class ContainerSet:
    def __init__(self, *values, contains_epsilon=False):
        self.set = set(values)
        self.contains_epsilon = contains_epsilon

    def add(self, value):
        n = len(self.set)
        self.set.add(value)
        return n != len(self.set)

    def extend(self, values):
        change = False
        for value in values:
            change |= self.add(value)
        return change

    def set_epsilon(self, value=True):
        last = self.contains_epsilon
        self.contains_epsilon = value
        return last != self.contains_epsilon

    def update(self, other):
        n = len(self.set)
        self.set.update(other.set)
        return n != len(self.set)

    def epsilon_update(self, other):
        return self.set_epsilon(self.contains_epsilon | other.contains_epsilon)

    def hard_update(self, other):
        return self.update(other) | self.epsilon_update(other)

    def find_match(self, match):
        for item in self.set:
            if item == match:
                return item
        return None

    def __len__(self):
        return len(self.set) + int(self.contains_epsilon)

    def __str__(self):
        return '%s-%s' % (str(self.set), self.contains_epsilon)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self.set)

    def __nonzero__(self):
        return len(self) > 0

    def __eq__(self, other):
        if isinstance(other, set):
            return self.set == other
        return isinstance(other, ContainerSet) and self.set == other.set and self.contains_epsilon == other.contains_epsilon


def inspect(item, grammar_name='G', mapper=None):
    try:
        return mapper[item]
    except (TypeError, KeyError ):
        if isinstance(item, dict):
            items = ',\n   '.join(f'{inspect(key, grammar_name, mapper)}: {inspect(value, grammar_name, mapper)}' for key, value in item.items() )
            return f'{{\n   {items} \n}}'
        elif isinstance(item, ContainerSet):
            args = f'{ ", ".join(inspect(x, grammar_name, mapper) for x in item.set) } ,' if item.set else ''
            return f'ContainerSet({args} contains_epsilon={item.contains_epsilon})'
        elif isinstance(item, EOF):
            return f'{grammar_name}.EOF'
        elif isinstance(item, Epsilon):
            return f'{grammar_name}.Epsilon'
        elif isinstance(item, Symbol):
            return f"G['{item.Name}']"
        elif isinstance(item, Sentence):
            items = ', '.join(inspect(s, grammar_name, mapper) for s in item._symbols)
            return f'Sentence({items})'
        elif isinstance(item, Production):
            left = inspect(item.Left, grammar_name, mapper)
            right = inspect(item.Right, grammar_name, mapper)
            return f'Production({left}, {right})'
        elif isinstance(item, tuple) or isinstance(item, list):
            ctor = ('(', ')') if isinstance(item, tuple) else ('[',']')
            return f'{ctor[0]} {("%s, " * len(item)) % tuple(inspect(x, grammar_name, mapper) for x in item)}{ctor[1]}'
        else:
            raise ValueError(f'Invalid: {item}')

def pprint(item, header=""):
    if header:
        print(header)

    if isinstance(item, dict):
        for key, value in item.items():
            print(f'{key}  --->  {value}')
    elif isinstance(item, list):
        print('[')
        for x in item:
            print(f'   {repr(x)}')
        print(']')
    else:
        print(item)


try:
    import pydot
except:
    pass

class State:
    def __init__(self, state, final=False, formatter=lambda x: str(x), shape='circle', tag=None):
        self.state = state
        self.final = final
        self.transitions = {}
        self.epsilon_transitions = set()
        self.tag = tag
        self.formatter = formatter
        self.shape = shape

    # The method name is set this way from compatibility issues.
    def set_formatter(self, value, attr='formatter', visited=None):
        if visited is None:
            visited = set()
        elif self in visited:
            return

        visited.add(self)
        self.__setattr__(attr, value)
        for destinations in self.transitions.values():
            for node in destinations:
                node.set_formatter(value, attr, visited)
        for node in self.epsilon_transitions:
            node.set_formatter(value, attr, visited)
        return self

    def has_transition(self, symbol):
        return symbol in self.transitions

    def add_transition(self, symbol, state):
        try:
            self.transitions[symbol].append(state)
        except:
            self.transitions[symbol] = [state]
        return self

    def add_epsilon_transition(self, state):
        self.epsilon_transitions.add(state)
        return self

    def recognize(self, string):
        states = self.epsilon_closure
        for symbol in string:
            states = self.move_by_state(symbol, *states)
            states = self.epsilon_closure_by_state(*states)
        return any(s.final for s in states)

    def to_deterministic(self, formatter=lambda x: str(x)):
        closure = self.epsilon_closure
        start = State(tuple(closure), any(s.final for s in closure), formatter)

        closures = [ closure ]
        states = [ start ]
        pending = [ start ]

        while pending:
            state = pending.pop()
            symbols = { symbol for s in state.state for symbol in s.transitions }

            for symbol in symbols:
                move = self.move_by_state(symbol, *state.state)
                closure = self.epsilon_closure_by_state(*move)

                if closure not in closures:
                    new_state = State(tuple(closure), any(s.final for s in closure), formatter)
                    if len(closure) == 1:
                        new_state = State(closure, any(s.final for s in closure), formatter)
                    closures.append(closure)
                    states.append(new_state)
                    pending.append(new_state)
                else:
                    index = closures.index(closure)
                    new_state = states[index]

                state.add_transition(symbol, new_state)

        return start

    @staticmethod
    def from_nfa(nfa, get_states=False):
        states = []
        for n in range(nfa.states):
            state = State(n, n in nfa.finals)
            states.append(state)

        for (origin, symbol), destinations in nfa.map.items():
            origin = states[origin]
            origin[symbol] = [ states[d] for d in destinations ]

        if get_states:
            return states[nfa.start], states
        return states[nfa.start]

    @staticmethod
    def move_by_state(symbol, *states):
        a = { s for state in states if state.has_transition(symbol) for s in state[symbol]}
        if len(a) == 1:
            a = a.pop()
        
        return a

    @staticmethod
    def epsilon_closure_by_state(*states):
        closure = { state for state in states }
        tmp = [s for s in closure]
        
        # print(f'\n\n Estoy en el metodo epsilon_closure_by_state y tengo {tmp} estados')
        # print(f'Mi primer estado {tmp[0]} tiene {tmp[0].epsilon_transitions} epsilon transiciones')
        
        for s in tmp:
            for epsilon_state in s.epsilon_transitions:
                    closure.add(epsilon_state)
        return closure

    @property
    def epsilon_closure(self):
        return self.epsilon_closure_by_state(self)

    @property
    def name(self):
        return self.formatter(self.state)

    def get(self, symbol):
        target = self.transitions[symbol]
        assert len(target) == 1
        return target[0]

    def __getitem__(self, symbol):
        if symbol == '':
            return self.epsilon_transitions
        try:
            return self.transitions[symbol]
        except KeyError:
            return None

    def __setitem__(self, symbol, value):
        if symbol == '':
            self.epsilon_transitions = value
        else:
            self.transitions[symbol] = value

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.state)

    def __hash__(self):
        return hash(self.state)

    def __iter__(self):
        yield from self._visit()

    def _visit(self, visited=None):
        if visited is None:
            visited = set()
        elif self in visited:
            return

        visited.add(self)
        yield self

        for destinations in self.transitions.values():
            for node in destinations:
                yield from node._visit(visited)
        for node in self.epsilon_transitions:
            yield from node._visit(visited)

    def graph(self):
        G = pydot.Dot(rankdir='LR', margin=0.1)
        G.add_node(pydot.Node('start', shape='plaintext', label='', width=0, height=0))

        visited = set()
        def visit(start):
            ids = id(start)
            if ids not in visited:
                visited.add(ids)
                G.add_node(pydot.Node(ids, label=start.name, shape=self.shape, style='bold' if start.final else ''))
                for tran, destinations in start.transitions.items():
                    for end in destinations:
                        visit(end)
                        G.add_edge(pydot.Edge(ids, id(end), label=tran, labeldistance=2))
                for end in start.epsilon_transitions:
                    visit(end)
                    G.add_edge(pydot.Edge(ids, id(end), label='ε', labeldistance=2))

        visit(self)
        G.add_edge(pydot.Edge('start', id(self), label='', style='dashed'))

        return G

    def _repr_svg_(self):
        try:
            return self.graph().create_svg().decode('utf8')
        except:
            pass

    def write_to(self, fname):
        return self.graph().write_svg(fname)



def multiline_formatter(state):
    return '\n'.join(str(item) for item in state)

def lr0_formatter(state):
    try:
        return '\n'.join(str(item)[:-4] for item in state)
    except TypeError:
        return str(state)[:-4]
    



class DisjointSet:
    def __init__(self, *items):
        self.nodes = { x: DisjointNode(x) for x in items }

    def merge(self, items):
        items = (self.nodes[x] for x in items)
        try:
            head, *others = items
            for other in others:
                head.merge(other)
        except ValueError:
            pass

    @property
    def representatives(self):
        return { n.representative for n in self.nodes.values() }

    @property
    def groups(self):
        return [[n for n in self.nodes.values() if n.representative == r] for r in self.representatives]

    def __len__(self):
        return len(self.representatives)

    def __getitem__(self, item):
        return self.nodes[item]

    def __str__(self):
        return str(self.groups)

    def __repr__(self):
        return str(self)

class DisjointNode:
    def __init__(self, value):
        self.value = value
        self.parent = self

    @property
    def representative(self):
        if self.parent != self:
            self.parent = self.parent.representative
        return self.parent

    def merge(self, other):
        other.representative.parent = self.representative

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)