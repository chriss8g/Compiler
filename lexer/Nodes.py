from lexer.automate import *

class Node:
    def evaluate(self):
        raise NotImplementedError()
        
class AtomicNode(Node):
    def __init__(self, lex):
        self.lex = lex

class UnaryNode(Node):
    def __init__(self, node):
        self.node = node
        
    def evaluate(self):
        value = self.node.evaluate() 
        return self.operate(value)
    
    @staticmethod
    def operate(value):
        raise NotImplementedError()
        
class BinaryNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def evaluate(self):
        lvalue = self.left.evaluate() 
        rvalue = self.right.evaluate()
        return self.operate(lvalue, rvalue)
    
    @staticmethod
    def operate(lvalue, rvalue):
        raise NotImplementedError()
    


EPSILON = 'ε'
class EpsilonNode(AtomicNode):
    def evaluate(self):
        nfa = NFA(states=2, finals=[1], transitions={
            (0,'ε'):[1]
        })    
        return nfa

class SymbolNode(AtomicNode):
    def evaluate(self):
        s = self.lex
        nfa = NFA(states=2, finals=[1], transitions={
            (0,s):[1]
        })
        return nfa
       
class ClosureNode(UnaryNode):
    @staticmethod
    def operate(value : NFA):
        nfa = automata_closure(value)
        return nfa
    
class UnionNode(BinaryNode):
    @staticmethod
    def operate(lvalue, rvalue):
        nfa = automata_union(lvalue,rvalue)
        return nfa

class ConcatNode(BinaryNode):
    @staticmethod
    def operate(lvalue, rvalue):
        nfa = automata_concatenation(lvalue,rvalue)
        return nfa