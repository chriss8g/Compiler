import cmp.visitor as visitor
from my_types import *
from scope import Scope

class SemanticCheckerVisitor(object):
    def __init__(self):
        self.errors = []
    
    @visitor.on('node')
    def visit(self, node, scope):
        pass
    
    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        scope = Scope() if not scope else scope
        for nod in node.statements:
            self.visit(nod, scope.create_child_scope())
        return self.errors
    
    @visitor.when(VarDeclarationNode)
    def visit(self, node, scope):

        for i in range(len(node.ids)):

            if(scope.is_var_defined(node.ids[i])):
                self.errors.append(f"Variable {node.ids[i]} doblemente declarada!")

            scope.define_variable(node.ids[i])

        child = scope.create_child_scope()
        self.visit(node.body, child)
        return self.errors
    
    @visitor.when(FuncDeclarationNode)
    def visit(self, node, scope):
        if(scope.is_func_defined(node.id, len(node.params))):
            self.errors.append(f"Funcion {node.id} doblemente declarada!")
        
        scope.parent.define_function(node.id, len(node.params))

        child = scope.create_child_scope()
        self.visit(node.body, child)
        
        return self.errors
    
    @visitor.when(PrintNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope.create_child_scope())
        return self.errors
    
    @visitor.when(ConstantNumNode)
    def visit(self, node, scope):
        return self.errors
    
    @visitor.when(VariableNode)
    def visit(self, node, scope):
        if(not scope.is_var_defined(node.lex)):
            self.errors.append(f"Variable {node.lex} no declarada!")
        return self.errors
    
    @visitor.when(CallNode)
    def visit(self, node, scope):
        if(not scope.is_func_defined(node.lex, len(node.args))):
            self.errors.append(f"Funcion {node.lex} no declarada!")

        for arg in node.args:
            self.visit(arg, scope.create_child_scope())
            
        return self.errors
    
    @visitor.when(BinaryNode)
    def visit(self, node, scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
