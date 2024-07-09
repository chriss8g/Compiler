from nodes_types import hulk_types as hulk
import nodes_types.cil as cil
from utils.base_CIL_visitor import BaseHULKToCILVisitor
import utils.visitor as visitor
from semantic_checker.scope import Scope, VariableInfo


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
            izq = attribute.id.name + \
                ".".join(attribute.id.child if attribute.id.child else [])
            self.current_type.attributes.append(
                cil.AssignNode(izq, attribute.value.lex))

        for method in node.body.methods:
            function_name = self.to_function_name_in_type(
                method.name, node.name)

            method.name = function_name
            self.visit(method, scope)

            text = function_name + '(' + ".".join(method.params) + ');'
            self.current_type.methods.append(text)

        self.current_type = parent_type

    @visitor.when(hulk.MethodNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')

        parent = self.current_function

        # function_name = self.to_function_name_in_type(node.name, node.type)
        self.current_function = self.register_function(node.name)

        for param in node.params:
            # vinfo = scope.find_variable(param)
            param_node = cil.ParamNode(param[0])
            self.register_param(param_node)

        expr = self.visit(node.body, scope)

        self.register_instruction(cil.ReturnNode(expr))

        self.current_function = parent

    @visitor.when(hulk.ObjectCreationNode)
    def visit(self, node, scope):
        
        dest = self.define_internal_local(node.type + '*')
        typex = cil.TypeNode('object')
        for x in self.dottypes:
            if x.name == node.type:
                typex = x
        self.register_instruction(cil.AllocateNode(typex, dest))
        return dest

    @visitor.when(hulk.FuncDeclarationNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')

        parent = self.current_function

        # function_name = self.to_function_name_in_type(node.name, node.type)
        self.current_function = self.register_function(node.name)

        for param in node.params:
            # vinfo = scope.find_variable(param)
            param_node = cil.ParamNode(param[0], param[1])
            self.register_param(param_node)

        expr = self.visit(node.body, scope)

        self.register_instruction(cil.ReturnNode(expr))

        self.current_function = parent

    @visitor.when(hulk.PrintNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')
        source = self.visit(node.expr, scope)
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.OurFunctionNode(
            'printf', dest, source, node.type))
        return dest

    @visitor.when(hulk.SinNode)
    def visit(self, node, scope):
        source = self.visit(node.expr, scope)
        dest = self.define_internal_local(node.type)
        self.register_instruction(
            cil.OurFunctionNode('sin', dest, source, node.type))
        return dest

    @visitor.when(hulk.CosNode)
    def visit(self, node, scope):
        source = self.visit(node.expr, scope)
        dest = self.define_internal_local(node.type)
        self.register_instruction(
            cil.OurFunctionNode('cos', dest, source, node.type))
        return dest

    @visitor.when(hulk.ExpNode)
    def visit(self, node, scope):
        source = self.visit(node.expr, scope)
        dest = self.define_internal_local(node.type)
        self.register_instruction(
            cil.OurFunctionNode('exp', dest, source, node.type))
        return dest

    @visitor.when(hulk.SqrtNode)
    def visit(self, node, scope):
        source = self.visit(node.expr, scope)
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.OurFunctionNode(
            'sqrt', dest, source, node.type))
        return dest

    # @visitor.when(hulk.AssignNode)
    # def visit(self, node, scope):

    #     vinfo = scope.find_variable(node.id)
    #     self.visit(node.expr, scope)
    #     dest = self.define_internal_local()
    #     source = cil.LocalNode(vinfo.name)
    #     self.register_instruction(cil.AssignNode(dest, source))

    @visitor.when(hulk.ConcatNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'

        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)

        dest = self.define_internal_local(node.type)

        dest2 = self.define_internal_local(node.type)
        self.register_instruction(cil.OurFunctionNode('concat', dest2, left, node.type, right))

        self.register_instruction(cil.AssignNode(dest, dest2))
        return dest

    @visitor.when(hulk.PlusNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, f"{left} + {right}"))
        return dest

    @visitor.when(hulk.MinusNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, f"{left} - {right}"))
        return dest

    @visitor.when(hulk.StarNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, f"{left} * {right}"))
        return dest

    @visitor.when(hulk.DivNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, f"{left} / {right}"))
        return dest

    @visitor.when(hulk.ModNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, f"{left} % {right}"))
        return dest

    @visitor.when(hulk.EQNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(hulk.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} == {right}"))
        return dest

    @visitor.when(hulk.GENode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(hulk.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} >= {right}"))
        return dest

    @visitor.when(hulk.GTNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(hulk.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} > {right}"))
        return dest

    @visitor.when(hulk.LENode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(hulk.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} <= {right}"))
        return dest

    @visitor.when(hulk.LTNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(hulk.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} < {right}"))
        return dest

    @visitor.when(hulk.IfNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        condition = self.visit(node.condition, scope.create_child_scope())

        self.register_instruction(cil.GotoNode('my_begin'))

        self.register_instruction(cil.LabelNode('my_if'))
        expr = self.visit(node.body, scope.create_child_scope())
        self.register_instruction(cil.GotoNode('my_end'))

        self.register_instruction(cil.LabelNode('my_else'))
        else_expr = self.visit(node.else_body, scope.create_child_scope())
        self.register_instruction(cil.GotoNode('my_end'))

        self.register_instruction(cil.LabelNode('my_begin'))
        self.register_instruction(
            cil.GotoIfNode(condition, 'my_if', 'my_else'))
        self.register_instruction(cil.LabelNode('my_end'))

    @visitor.when(hulk.DestructNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')

        x = scope.get_variable_info(node.id.name) if scope.get_variable_info(
            node.id.name) else node.id
        expr = self.visit(node.expr, scope.create_child_scope())
        self.register_instruction(cil.AssignNode(x, expr))
        return expr

    @visitor.when(hulk.WhileNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')
        self.register_instruction(cil.GotoNode('while_label'))
        self.register_instruction(cil.LabelNode('body'))
        self.visit(node.body, scope.create_child_scope())
        self.register_instruction(cil.LabelNode('while_label'))
        condition = self.visit(node.condition, scope.create_child_scope())
        self.register_instruction(cil.GotoIfNode(
            condition, 'body', 'endwhile_label'))
        self.register_instruction(cil.LabelNode('endwhile_label'))

    @visitor.when(hulk.NumberNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')
        # print(node.type)
        source = node.lex
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, source))
        return dest

    @visitor.when(hulk.StringNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')
        source = node.lex
        msg = self.register_data(source)
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.LoadNode(dest, msg))
        # self.register_instruction(cil.AssignNode(dest, source))
        return dest

    @visitor.when(hulk.BlockNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')

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
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')

        parent = self.current_function

        name = self.to_function_name('block')

        self.current_function = self.register_function(name)

        local_names = []
        for arg in parent.params:
            self.register_param(arg)

            dest = self.define_internal_local(arg.type)
            local_names.append(dest)
            scope.dict[arg.name] = dest
            scope.define_variable(arg.name)
            self.register_instruction(cil.AssignNode(dest, arg.name))


        for child in node.args:

            child.type = child.type if child.type != hulk.BOOL_TYPE else hulk.INT_TYPE
            child.type = child.type if child.type != hulk.STRING_TYPE else 'char*'
            child.type = child.type if child.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (child.type + '*')

            self.register_param(cil.ParamNode(child.id.name, child.type))

            dest = self.define_internal_local(child.type)
            local_names.append(dest)
            scope.dict[child.id.name] = dest
            scope.define_variable(child.id.name)

            self.register_instruction(cil.AssignNode(dest, child.id.name))

        if (isinstance(node.body, hulk.BlockNode)):
            for child in node.body.body:
                expr = self.visit(child, scope.create_child_scope())
        else:
            # print(scope.dict)
            expr = self.visit(node.body, scope.create_child_scope())

        self.register_instruction(cil.ReturnNode(expr))
        self.current_function = parent
        scope = scope.parent

        temp = f'{name}(' + ", ".join(child.name for child in parent.params) + (', ' if len(parent.params) else "") + ", ".join(self.visit(child.expr, scope.create_child_scope()) for child in node.args) + ")"
        dest = self.define_internal_local(node.body.type)
        self.register_instruction(cil.AssignNode(dest, temp))

        return dest

    @visitor.when(hulk.IdentifierNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')
        
        
        child = node.child
        
        func = ''
        if(child):
            func = self.to_function_name_in_type(child.name, node.type[:-1])
            func += '(' + ", ".join(child.args) + ')'
        else:
            func = scope.get_variable_info(
                node.name) if scope.get_variable_info(node.name) else node.name

            
        

        # while (child):
        #     elemt += "." + child.id + '(' + ".".join(child.args) + ');'
        #     child = child.child


        return func

    @visitor.when(hulk.CallNode)
    def visit(self, node, scope):
        node.type = node.type if node.type != hulk.BOOL_TYPE else hulk.INT_TYPE
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        node.type = node.type if node.type in ['char*', hulk.NUMBER_TYPE, hulk.INT_TYPE] else (node.type + '*')

        params = []
        for child in node.args:
            params.append(self.visit(child, scope.create_child_scope()))

        temp = f'{node.name}(' + ", ".join(child for child in params) + ")"
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, temp))

        return dest
