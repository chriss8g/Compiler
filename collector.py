import utils.visitor as visitor
from nodes_types import hulk_types as hulk
from utils.semantic import Context
from semantic_checker.scope import Scope

class Collector(object):
    def __init__(self, errors=[], scope = None):
        self.context = None
        self.errors = errors
    
    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(hulk.ProgramNode)
    def visit(self, node, scope = None):
        scope = Scope() if not scope else scope
        self.context = Context()
        for statement in node.statements:
            self.visit(statement, scope.create_child_scope())
        self.visit(node.main, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.FuncDeclarationNode)
    def visit(self, node, scope):
        sub_scope = scope.create_child_scope()
        for param in node.params:
            sub_scope.define_variable(param[0],param[1])
        self.visit(node.body, sub_scope)
        try:
            self.context.create_func(node.name)
        except:
            self.errors.append(f"La Función '{node.name}' ha sido definida más de una vez.")
        return self.errors
        
            
    @visitor.when(hulk.TypeDeclarationNode)
    def visit(self, node, scope):
        try:
            self.context.create_type(node.name)
        except:
            self.errors.append(f"La clase '{node.name}' ha sido definida más de una vez.")
        body_scope = scope.create_child_scope()
        for param in node.params:
            body_scope.define_variable(param[0],param[1])
        for param in node.base_params:
            body_scope.define_variable(param[0],param[1])
        self.visit(node.body, body_scope)
        return self.errors
    
    @visitor.when(hulk.TypeBodyDeclarationNode)
    def visit(self, node, scope):
        sub_scope = scope.create_child_scope()
        for attr in node.attributes:
            if not sub_scope.is_var_defined(attr.name.name):
                self.visit(attr, sub_scope)
                sub_scope.define_variable(attr.name.name,attr.type)
            else:
                self.errors.append(f"El atributo '{attr.name.name}' ha sido definido más de una vez")
        for meth in node.methods:
            if not sub_scope.is_func_defined(meth.name,len(meth.params)):
                sub_scope.define_function(meth.name,meth.params)
            else:
                self.errors.append(f"El método '{meth.name}' con '{len(meth.params)}' parámetros ha sido definido más de una vez")
        for meth in node.methods:
            self.visit(meth, sub_scope)
        return self.errors
    
    @visitor.when(hulk.AttributeNode)
    def visit(self, node, scope):
        self.visit(node.value, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.MethodNode)
    def visit(self, node, scope):
        sub_scope = scope.create_child_scope()
        for param in node.params:
            sub_scope.define_variable(param[0],param[1])
        self.visit(node.body, sub_scope)
        return self.errors
    
    @visitor.when(hulk.AssignNode)
    def visit(self,node,scope):
        self.visit(node.id, scope.create_child_scope())
        self.visit(node.expr, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.PrintNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope.create_child_scope())
        return self.errors

    @visitor.when(hulk.BlockNode)
    def visit(self,node,scope):
        for expr in node.body:
            self.visit(expr,scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.LetNode)
    def visit(self, node, scope):
        for var in node.args:
            sub_scope = scope.create_child_scope()
            sub_scope.define_variable(var.id.name)
            # print(sub_scope.local_vars)
            self.visit(var.id, sub_scope)
            scope.define_variable(var.id.name)
            # print(var.id.name)
            self.visit(var.expr, scope.create_child_scope())
        self.visit(node.body, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.WhileNode)
    def visit(self,node,scope):
        self.visit(node.condition, scope.create_child_scope())
        self.visit(node.body, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.IfNode)
    def visit(self,node,scope):
        self.visit(node.condition, scope.create_child_scope())
        self.visit(node.body, scope.create_child_scope())
        self.visit(node.else_body, scope.create_child_scope())
        for cond in node.elif_conditions:
            self.visit(cond, scope.create_child_scope())
        for body in node.elif_body:
            self.visit(body, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.DestructNode)
    def visit(self,node,scope):
        self.visit(node.id, scope.create_child_scope())
        self.visit(node.expr, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.CallNode)
    def visit(self, node, scope):
        if is_func_defined(node.id, len(node.args)):
            for arg in node.args:
                self.visit(arg, scope.create_child_scope())
        else:
            self.errors(f"La función '{node.id}' no está definida")
        return self.errors
    
    @visitor.when(hulk.PlusNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.MinusNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.StarNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.DivNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.PowNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.ModNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors

    @visitor.when(hulk.EQNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.GTNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.LTNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.GENode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.LENode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.NENode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.AndNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.OrNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.NotNode)
    def visit(self,node,scope):
        self.visit(node.lex, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.ConcatNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.ConcatSpaceNode)
    def visit(self,node,scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.ObjectCreationNode)
    def visit(self,node,scope):
        for arg in node.args:
            self.visit(arg, scope.create_child_scope())
        return self.errors
    
    @visitor.when(hulk.IdentifierNode)
    def visit(self,node,scope):
        if not scope.is_var_defined(node.name):
            self.errors.append(f"Variable {node.name} no declarada")
        if node.child:
            self.visit(node.child, scope.create_child_scope())
        return self.errors
    
        #self
        
        @visitor.when(hulk.SinNode)
        def visit(self,node,scope):
            self.visit(node.expr, scope.create_child_scope())
            return self.errors
        
        @visitor.when(hulk.CosNode)
        def visit(self,node,scope):
            self.visit(node.expr, scope.create_child_scope())
            return self.errors
        
        @visitor.when(hulk.SqrtNode)
        def visit(self,node,scope):
            self.visit(node.expr, scope.create_child_scope())
            return self.errors
        
        @visitor.when(hulk.ExpNode)
        def visit(self,node,scope):
            self.visit(node.expr, scope.create_child_scope())
            return self.errors
        
        @visitor.when(hulk.LogNode)
        def visit(self,node,scope):
            self.visit(node.expr, scope.create_child_scope())
            return self.errors
        
        @visitor.when(hulk.RandNode)
        def visit(self,node,scope):
            pass
        
        @visitor.when(hulk.NumberNode)
        def visit(self,node,scope):
            pass
        
        @visitor.when(hulk.StringNode)
        def visit(self,node,scope):
            pass
        
        @visitor.when(hulk.BoolNode)
        def visit(self,node,scope):
            pass