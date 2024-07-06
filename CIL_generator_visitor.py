from nodes_types import hulk_types as hulk
import nodes_types.cil as cil
from utils.base_CIL_visitor import BaseHULKToCILVisitor
import utils.visitor as visitor
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

        parent_type = self.current_type

        type_node = self.register_type(node.name)

        self.current_type = type_node


        for attribute in node.body.attributes:
            izq = attribute.name.name + ".".join(attribute.name.child if attribute.name.child else [])
            self.current_type.attributes.append(cil.AssignNode(izq, attribute.value.lex))

        # for method in node.body.methods:
        #     function_name = self.to_function_name_in_type(method.name, method.type)
        #     self.current_type.methods.append(cil.AssignNode(function_name, attribute.value))

        self.current_type = parent_type

    @visitor.when(hulk.ObjectCreationNode)
    def visit(self, node, scope):
        dest = self.define_internal_local()
        for x in self.dottypes:
            if x.name == node.type:
                typex = x
        self.register_instruction(cil.AllocateNode(typex, dest))
        return dest

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
        source = self.visit(node.expr, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.OurFunctionNode('printf', dest, source))
        return dest

    @visitor.when(hulk.SinNode)
    def visit(self, node, scope):
        source = self.visit(node.expr, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.OurFunctionNode('sin', dest, source))
        return dest

    @visitor.when(hulk.CosNode)
    def visit(self, node, scope):
        source = self.visit(node.expr, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.OurFunctionNode('cos', dest, source))
        return dest

    @visitor.when(hulk.ExpNode)
    def visit(self, node, scope):
        source = self.visit(node.expr, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.OurFunctionNode('exp', dest, source))
        return dest
    
    @visitor.when(hulk.SqrtNode)
    def visit(self, node, scope):
        source = self.visit(node.expr, scope)
        dest = self.define_internal_local()
        self.register_instruction(cil.OurFunctionNode('sqrt', dest, source))
        return dest

    

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
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} - {right}"))
        return dest

    @visitor.when(hulk.StarNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} * {right}"))
        return dest

    @visitor.when(hulk.DivNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} / {right}"))
        return dest
    
    @visitor.when(hulk.ModNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} % {right}"))
        return dest
    
    @visitor.when(hulk.EQNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} == {right}"))
        return dest
    
    @visitor.when(hulk.GENode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} >= {right}"))
        return dest
    
    @visitor.when(hulk.GTNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} < {right}"))
        return dest
    
    @visitor.when(hulk.LENode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} >= {right}"))
        return dest
    
    @visitor.when(hulk.LTNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local()
        self.register_instruction(cil.AssignNode(dest, f"{left} > {right}"))
        return dest

    @visitor.when(hulk.IfNode)
    def visit(self, node, scope):
        condition = self.visit(node.condition, scope.create_child_scope())

        self.register_instruction(cil.GotoNode('my_begin'))

        self.register_instruction(cil.LabelNode('my_if'))
        expr = self.visit(node.body, scope.create_child_scope())
        self.register_instruction(cil.GotoNode('my_end'))

        self.register_instruction(cil.LabelNode('my_else'))
        else_expr = self.visit(node.else_body, scope.create_child_scope())
        self.register_instruction(cil.GotoNode('my_end'))


        self.register_instruction(cil.LabelNode('my_begin'))
        self.register_instruction(cil.GotoIfNode(condition, 'my_if', 'my_else'))
        self.register_instruction(cil.LabelNode('my_end'))

    @visitor.when(hulk.DestructNode)
    def visit(self, node, scope):

        x = scope.get_variable_info(node.id.name) if scope.get_variable_info(node.id.name) else node.id
        expr = self.visit(node.expr, scope.create_child_scope())
        self.register_instruction(cil.AssignNode(x, expr))

    @visitor.when(hulk.WhileNode)
    def visit(self, node, scope):
        self.register_instruction(cil.GotoNode('while_label'))
        self.register_instruction(cil.LabelNode('body'))
        self.visit(node.body, scope.create_child_scope())
        self.register_instruction(cil.LabelNode('while_label'))
        condition = self.visit(node.condition, scope.create_child_scope())
        self.register_instruction(cil.GotoIfNode(condition, 'body', 'endwhile_label'))
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
        elemt = scope.get_variable_info(node.name) if scope.get_variable_info(node.name) else node.name
        child = node.child
        while(child):
            elemt += "." + child.name
            child = child.child
        return elemt
    
    @visitor.when(hulk.CallNode)
    def visit(self, node, scope):

        params = []
        for child in node.args:
            params.append(self.visit(child, scope.create_child_scope()))

        return f'{node.id}(' + ", ".join(child for child in params) + ")"