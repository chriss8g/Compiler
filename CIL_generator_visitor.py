from nodes_types.hulk import *
import cil as cil
from base_CIL_visitor import BaseHULKToCILVisitor
import cmp.visitor as visitor
from semantic_checker.scope import Scope

class HULKToCILVisitor(BaseHULKToCILVisitor):
    @visitor.on('node')
    def visit(self, node):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        scope = Scope() if not scope else scope

        for _ in range(len(node.statements)):#!!!!
            scope.create_child_scope()

        self.current_function = self.register_function('main')

        for declaration, child_scope in zip(node.statements, scope.children):
            self.visit(declaration, child_scope)

        self.register_instruction(cil.ReturnNode(0))
        self.current_function = None

        return cil.ProgramNode(self.dottypes, self.dotdata, self.dotcode)

    @visitor.when(TypeNode)
    def visit(self, node, scope):
        self.current_type = self.context.get_type(node.id)
        type_node = self.register_type(node.id)

        for attr, xtype in self.current_type.all_attributes():
            type_node.attributes.append(attr.name)

        for method, xtype in self.current_type.all_methods():
            function_name = self.to_function_name_in_type(method.name, xtype.name)
            type_node.methods.append((method.name, function_name))

        func_declarations = (f for f in node.features if isinstance(f, FuncDeclarationNode))
        for feature, child_scope in zip(func_declarations, scope.children):
            self.visit(feature, child_scope)

        self.current_type = None

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, scope):
        function_name = self.to_function_name_in_type(node.id, self.current_type.name)
        self.current_function = self.register_function(function_name)

        for param in node.params:
            vinfo = scope.find_variable(param)
            param_node = cil.ParamNode(vinfo.name)
            self.params.append(param_node)

        self.visit(node.body, scope)

        self.current_function = self.dotcode[0]

    @visitor.when(PrintNode)
    def visit(self, node, scope):

        dest = self.visit(node.expr, scope)
        self.register_instruction(cil.PrintNode(dest))

    @visitor.when(AsignNode)
    def visit(self, node, scope, parent):

        vinfo = scope.find_variable(node.id)
        self.visit(node.expr, scope)
        dest = self.define_internal_local()
        source = cil.LocalNode(vinfo.name)
        self.register_instruction(cil.AssignNode(dest, source))


    @visitor.when(PlusNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.PlusNode(dest, left, right))
        return dest

    @visitor.when(MinusNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.MinusNode(dest, left, right))
        return dest

    @visitor.when(StarNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.StarNode(dest, left, right))
        return dest

    @visitor.when(DivNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.DivNode(dest, left, right))
        return dest
    
    @visitor.when(EqualNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} == {right}"))
        return dest

    @visitor.when(IfNode)
    def visit(self, node, scope):
        condition = self.visit(node.condition, scope)
        expr = self.visit(node.expr, scope)
        else_expr = self.visit(node.else_expr, scope)

        # if node.else_expr:
        #     self.register_instruction(cil.LabelNode('else_label'))
        #     self.visit(node.else_expr, scope)
        self.register_instruction(cil.IfNode(condition, expr, else_expr))

    @visitor.when(WhileNode)
    def visit(self, node, scope):
        self.register_instruction(cil.LabelNode('while_label'))
        condition = self.visit(node.condition, scope)
        self.register_instruction(cil.GotoIfNode(condition))
        self.visit(node.expr, scope)
        self.register_instruction(cil.GotoNode('while_label'))
        self.register_instruction(cil.LabelNode('endwhile_label'))

    @visitor.when(ConstantNumNode)
    def visit(self, node, scope):
        dest = self.define_internal_local()
        source = node.lex
        self.register_instruction(cil.AssignNode(dest, source))
        return dest

    @visitor.when(BlockNode)
    def visit(self, node, scope):
        
        parent = self.current_function

        name = self.to_function_name('block')

        self.current_function = self.register_function(name)
        for i in node.body:
            self.visit(i, scope)
        self.register_instruction(cil.ReturnNode(0))
        
        self.current_function = parent

        return name