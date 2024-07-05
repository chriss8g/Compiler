from nodes_types import hulk_types as hulk
import cil as cil
from base_CIL_visitor import BaseHULKToCILVisitor
import cmp.visitor as visitor
from semantic_checker.scope import Scope

class HULKToCILVisitor(BaseHULKToCILVisitor):
    @visitor.on('node')
    def visit(self, node):
        pass

    @visitor.when(hulk.ProgramNode)
    def visit(self, node, scope=None):
        scope = Scope() if not scope else scope

        for child in node.statements:
            self.visit(child, scope.create_child_scope())

        self.current_function = self.register_function('main')

        self.visit(node.main, scope.create_child_scope())

        self.register_instruction(cil.ReturnNode(0))
        self.current_function = None

        return cil.ProgramNode(self.dottypes, self.dotdata, self.dotcode)

    @visitor.when(hulk.TypeDeclarationNode)
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

    @visitor.when(hulk.FuncDeclarationNode)
    def visit(self, node, scope):

        parent = self.current_function
            

        # function_name = self.to_function_name_in_type(node.name, node.type)
        self.current_function = self.register_function(node.name)

        for param in node.params:
            # vinfo = scope.find_variable(param)
            param_node = cil.ParamNode(param[0])
            self.params.append(param_node)

        expr = self.visit(node.body, scope)

        self.register_instruction(cil.ReturnNode(expr))
        
        self.current_function = parent

    @visitor.when(hulk.PrintNode)
    def visit(self, node, scope):
        # print(node.expr)
        dest = self.visit(node.expr, scope)
        self.register_instruction(cil.PrintNode(dest))

    @visitor.when(hulk.AssignNode)
    def visit(self, node, scope):

        vinfo = scope.find_variable(node.id)
        self.visit(node.expr, scope)
        dest = self.define_internal_local()
        source = cil.LocalNode(vinfo.name)
        self.register_instruction(cil.AssignNode(dest, source))


    @visitor.when(hulk.PlusNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} + {right}"))
        return dest

    @visitor.when(hulk.MinusNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.MinusNode(dest, left, right))
        return dest

    @visitor.when(hulk.StarNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.StarNode(dest, left, right))
        return dest

    @visitor.when(hulk.DivNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.DivNode(dest, left, right))
        return dest
    
    @visitor.when(hulk.EQNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} == {right}"))
        return dest

    @visitor.when(hulk.IfNode)
    def visit(self, node, scope):
        condition = self.visit(node.condition, scope)

        self.register_instruction(cil.GotoNode('my_begin'))

        self.register_instruction(cil.LabelNode('my_if'))
        expr = self.visit(node.body, scope)
        self.register_instruction(cil.GotoNode('my_end'))

        self.register_instruction(cil.LabelNode('my_else'))
        else_expr = self.visit(node.else_body, scope)
        self.register_instruction(cil.GotoNode('my_end'))


        self.register_instruction(cil.LabelNode('my_begin'))
        self.register_instruction(cil.GotoIfNode(condition, 'my_if', 'my_else'))
        self.register_instruction(cil.LabelNode('my_end'))

        

        # if node.else_expr:
            # self.register_instruction(cil.LabelNode('else_label'))
        #     self.visit(node.else_expr, scope)
        # self.register_instruction(cil.IfNode(condition, expr, else_expr))



    @visitor.when(hulk.WhileNode)
    def visit(self, node, scope):
        self.register_instruction(cil.LabelNode('while_label'))
        condition = self.visit(node.condition, scope)
        self.register_instruction(cil.GotoIfNode(condition))
        self.visit(node.expr, scope)
        self.register_instruction(cil.GotoNode('while_label'))
        self.register_instruction(cil.LabelNode('endwhile_label'))

    @visitor.when(hulk.NumberNode)
    def visit(self, node, scope):
        dest = self.define_internal_local()
        source = node.lex
        self.register_instruction(cil.AssignNode(dest, source))
        return dest

    @visitor.when(hulk.BlockNode)
    def visit(self, node, scope):
        
        # parent = self.current_function

        # name = self.to_function_name('block')

        # self.current_function = self.register_function(name)
        for i in node.body:
            name = self.visit(i, scope)
        # self.register_instruction(cil.ReturnNode(0))
        
        # self.current_function = parent

        return name
    
    
    
    @visitor.when(hulk.LetNode)
    def visit(self, node, scope):

        parent = self.current_function

        name = self.to_function_name('block')

        self.current_function = self.register_function(name)
        



        local_names = []
        for child in node.args:
            dest = self.define_internal_local()
            local_names.append(dest)
            scope.dict[child.id.name] = dest
            scope.define_variable(child.id.name)
            values = self.visit(child.expr, scope.create_child_scope())
            self.register_instruction(cil.AssignNode(dest, values))

        if(isinstance(node.body, hulk.BlockNode)):
            for child in node.body.body:
                expr = self.visit(child, scope.create_child_scope()) 
        else:
            # print(scope.dict)
            expr = self.visit(node.body, scope.create_child_scope())



        self.register_instruction(cil.ReturnNode(expr))       
        self.current_function = parent

        dest = self.define_internal_local()
        self.register_instruction(cil.StaticCallNode(name, dest))

        return dest
    
    @visitor.when(hulk.IdentifierNode)
    def visit(self, node, scope):

        return scope.get_variable_info(node.name) if scope.get_variable_info(node.name) else node.name

    @visitor.when(hulk.CallNode)
    def visit(self, node, scope):

        params = []
        for child in node.args:
            params.append(self.visit(child, scope.create_child_scope()))

        return f'{node.id}(' + ", ".join(child for child in params) + ")"