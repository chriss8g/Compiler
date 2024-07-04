
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

    @visitor.when(AsignNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope.create_child_scope())
        # print(node.id)
        if(node.id.type != node.expr.type):
            self.errors.append(f"Variable {node.id.lex} de tipo {node.id.type} no puede guardar el tipo {node.expr.type}")

        return self.errors

    @visitor.when(VarDeclarationNode)
    def visit(self, node, scope):
        for var in node.args:
            if scope.is_local_var(var.id.lex):
                self.errors.append(f"Variable {var.id.lex} doblemente declarada!")
            else:
                sub_scope = scope.create_child_scope()
                sub_scope.define_variable(var.id.lex)
                self.visit(var.id, sub_scope)
                scope.define_variable(var.id.lex)
                self.visit(var.expr, scope.create_child_scope())

        # print(self.errors)
        # print(scope.local_vars)
        self.visit(node.body, scope.create_child_scope())
        node.type = node.body.type
        return self.errors

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, scope):
        if scope.is_func_defined(node.id, len(node.params)):
            self.errors.append(f"Funcion {node.id} doblemente declarada!")
        else:
            scope.define_function(node.id, len(node.params))
        child_scope = scope.create_child_scope()
        for param in node.params:
            child_scope.define_variable(param)
        self.visit(node.body, child_scope)
        node.type = node.body.type
        return self.errors

    @visitor.when(PrintNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope.create_child_scope())
        return self.errors

    @visitor.when(ConstantNumNode)
    def visit(self, node, scope):
        node.type = INT_TYPE
        return self.errors

    @visitor.when(VariableNode)
    def visit(self, node, scope):
        if not scope.is_var_defined(node.lex) :
            self.errors.append(f"Variable {node.lex} no declarada!")
        return self.errors

    @visitor.when(CallNode)
    def visit(self, node, scope):
        if not scope.is_func_defined(node.id, len(node.args)):
            self.errors.append(f"Funcion {node.id} no declarada!")
        for arg in node.args:
            self.visit(arg, scope.create_child_scope())
        return self.errors

    @visitor.when(DivNode)
    def visit(self, node, scope):
        self.visit(node.left, scope.create_child_scope())
        if self.visit(node.right, scope.create_child_scope()) == 0:
            self.errors.append("No puede dividir por cero!!")
        node.type = FLOAT_TYPE
        return self.errors

    @visitor.when(PowNode)
    def visit(self, node, scope):
        self.visit(node.left, scope.create_child_scope())
        self.visit(node.right, scope.create_child_scope())
        node.type = FLOAT_TYPE
        return self.errors

    @visitor.when(BinaryNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        self.visit(node.right, scope)
        if isinstance(node, (PlusNode, MinusNode, StarNode, DivNode, PowNode, ModNode)):
            if node.left.type not in NUMBER_TYPE or node.right.type not in NUMBER_TYPE:
                self.errors.append(f"Tipos incompatibles en operación aritmética: {node.left.type} y {node.right.type}")
            node.type = FLOAT_TYPE if FLOAT_TYPE in [node.left.type, node.right.type] else INT_TYPE
        elif isinstance(node, (AndNode, OrNode)):
            if node.left.type != BOOL_TYPE or node.right.type != BOOL_TYPE:
                self.errors.append(f"Tipos incompatibles en operación lógica: {node.left.type} y {node.right.type}")
            node.type = BOOL_TYPE
        elif isinstance(node, (EQNode, GTNode, LTNode, GENode, LENode, NENode)):
            if node.left.type != node.right.type:
                self.errors.append(f"Tipos incompatibles en operación comparativa: {node.left.type} y {node.right.type}")
            node.type = BOOL_TYPE
        elif isinstance(node, ConcatNode):
            if node.left.type != STRING_TYPE or node.right.type != STRING_TYPE:
                self.errors.append(f"Tipos incompatibles en operación de concatenación: {node.left.type} y {node.right.type}")
            node.type = STRING_TYPE
        return self.errors

    @visitor.when(IfNode)
    def visit(self, node, scope):
        self.visit(node.condition, scope)
        if node.condition.type != BOOL_TYPE:
            self.errors.append(f"Condición de if debe ser booleana, no {node.condition.type}")
        self.visit(node.expr, scope.create_child_scope())
        if node.else_expr:
            self.visit(node.else_expr, scope.create_child_scope())
        for cond, expr in zip(node.elif_conditions, node.elif_expr):
            self.visit(cond, scope.create_child_scope())
            if cond.type != BOOL_TYPE:
                self.errors.append(f"Condición de elif debe ser booleana, no {cond.type}")
            self.visit(expr, scope.create_child_scope())
        return self.errors

    @visitor.when(WhileNode)
    def visit(self, node, scope):
        self.visit(node.condition, scope)
        if node.condition.type != BOOL_TYPE:
            self.errors.append(f"Condición de while debe ser booleana, no {node.condition.type}")
        self.visit(node.expr, scope.create_child_scope())
        return self.errors

    @visitor.when(ForNode)
    def visit(self, node, scope):
        self.visit(node.iterable, scope)
        if node.iterable.type not in [INT_TYPE, FLOAT_TYPE]:
            self.errors.append(f"Iterador de for debe ser numérico, no {node.iterable.type}")
        child_scope = scope.create_child_scope()
        child_scope.define_variable(node.id)
        self.visit(node.expr, child_scope)
        return self.errors