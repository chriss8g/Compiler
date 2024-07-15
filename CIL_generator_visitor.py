from nodes_types import hulk_types as hulk
from nodes_types import c_type as c
import nodes_types.cil as cil
from utils.base_CIL_visitor import BaseHULKToCILVisitor
import utils.visitor as visitor
from semantic_checker.scope import Scope, VariableInfo


def update_types(type):
    type = type if type != hulk.BOOL_TYPE else c.INT_TYPE
    type = type if type != hulk.NUMBER_TYPE else c.FLOAT_TYPE
    type = type if type != hulk.STRING_TYPE else c.STRING_TYPE
    if (not type.endswith('*')):
        type = type if type in c.MY_TYPES else (type + '*')
    return type


class HULKToCILVisitor(BaseHULKToCILVisitor):

    def __init__(self, context):
        super().__init__(context)
        self.types = {}
        self.context2 = {}

    @visitor.on('node')
    def visit(self, node):
        pass

    @visitor.when(hulk.ProgramNode)
    def visit(self, node, scope=None):
        scope = Scope() if not scope else scope

        for child in node.statements:
            self.visit(child, scope.create_child_scope())

        self.current_function = self.register_function('main', c.INT_TYPE)

        self.visit(node.main, scope.create_child_scope())

        self.register_instruction(cil.ReturnNode(0))
        self.current_function = None

        return cil.ProgramNode(self.dottypes, self.dotdata, self.dotcode)

    @visitor.when(hulk.TypeDeclarationNode)
    def visit(self, node, scope):

        parent_type = self.current_type

        self.types[node.name] = node
        type_node = self.register_type(node.name)

        self.current_type = type_node

        if node.base_type and node.base_type != hulk.OBJECT_TYPE:
            

            parent = self.types[node.base_type]

            for attribute in parent.body.attributes:
                self.current_type.attributes.append(
                    cil.LocalNode(attribute.id.name, update_types(attribute.type)))
                sub_scope = scope.create_child_scope()
                self.visit(hulk.MethodNode(
                    f'init_{attribute.id.name}_of_{node.name}',
                    hulk.AssignNode(
                        hulk.IdentifierNode(
                            f'self->{attribute.id.name}',
                            None, attribute.id.type),
                        attribute.value,
                        'void'),
                    node.params + [('self', f'{node.name}*')],
                    attribute.value.type),
                    sub_scope)

            for method in parent.body.methods:
                its_methods = method.params[:-1]
                its_methods.append(('self', f'{node.name}*'))

                self.visit(method, scope.create_child_scope())

                function_name = self.to_function_name_in_type(
                    method.name, node.name)
                
                text = function_name + \
                    '(' + \
                    ".".join([f'{i[0]}:{i[1]}' for i in its_methods]) + ');'
                self.current_type.methods.append(text)

        for attribute in node.body.attributes:
            self.current_type.attributes.append(
                cil.LocalNode(attribute.id.name, update_types(attribute.type)))
            sub_scope = scope.create_child_scope()
            self.visit(hulk.MethodNode(
                f'init_{attribute.id.name}_of_{node.name}',
                hulk.AssignNode(
                    hulk.IdentifierNode(
                        f'self->{attribute.id.name}',
                        None, attribute.id.type),
                    attribute.value,
                    'void'),
                node.params + [('self', f'{node.name}*')],
                attribute.value.type),
                sub_scope)

        for method in node.body.methods:

            # if not node.base_type or node.base_type == hulk.OBJECT_TYPE:
            method.params.append(('self', f'{node.name}*'))

            self.visit(method, scope.create_child_scope())

            function_name = self.to_function_name_in_type(
                method.name, node.name)
            
            text = function_name + \
                '(' + \
                ".".join([f'{i[0]}:{i[1]}' for i in method.params]) + ');'
            self.current_type.methods.append(text)

        self.current_type = parent_type

    @visitor.when(hulk.MethodNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        parent = self.current_function

        function_name = self.to_function_name_in_type(node.name, self.current_type.name)
        self.context2[node.name] = function_name
        self.current_function = self.register_function(
            function_name, node.type)

        for param in node.params:
            # vinfo = scope.find_variable(param)
            param_node = cil.ParamNode(param[0])
            self.register_param(param_node)

        expr = self.visit(node.body, scope.create_child_scope())

        self.register_instruction(cil.ReturnNode(expr))

        self.current_function = parent

    @visitor.when(hulk.ObjectCreationNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        dest = self.define_internal_local(node.type)
        typex = cil.TypeNode('object')
        for x in self.dottypes:
            if (x.name+'*') == node.type:
                typex = x
        self.register_instruction(cil.AllocateNode(typex, dest))

        force = ''
        for i in self.context.get_type(node.type[:-1]).attributes:
            info = ', '.join([ arg.lex for arg in (node.args + [hulk.StringNode(dest)]) ])
            force += f'init_{i.name}_of_{self.context.get_type(node.type[:-1]).name}({info});\n'

        self.register_instruction(cil.Force(force))

        return dest

    @visitor.when(hulk.FuncDeclarationNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        parent = self.current_function

        function_name = self.to_function_name(node.name)
        self.context[node.name] = function_name
        self.current_function = self.register_function(
            function_name, node.type)

        for param in node.params:
            # vinfo = scope.find_variable(param)
            # print(param)
            name = self.to_param_name(param[0])
            scope.dict[param[0]] = name
            scope.define_variable(param[0], update_types(param[1]))
            param_node = cil.ParamNode(name, update_types(param[1]))
            self.register_param(param_node)

            dest = self.define_internal_local(update_types(param[1]))
            scope.dict[name] = dest
            scope.define_variable(name, update_types(param[1]))
            scope.define_variable(dest, update_types(param[1]))
            self.register_instruction(cil.AssignNode(dest, name))

        expr = self.visit(node.body, scope.create_child_scope())

        self.register_instruction(cil.ReturnNode(expr))

        self.current_function = parent

        return function_name

    @visitor.when(hulk.PrintNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        source = self.visit(node.expr, scope.create_child_scope())
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.OurFunctionNode(
            'printf', dest, source, node.type))
        return source

    @visitor.when(hulk.SinNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        source = self.visit(node.expr, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(
            cil.OurFunctionNode('sin', dest, source, node.type))
        return dest

    @visitor.when(hulk.CosNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        source = self.visit(node.expr, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(
            cil.OurFunctionNode('cos', dest, source, node.type))
        return dest

    @visitor.when(hulk.ExpNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        source = self.visit(node.expr, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(
            cil.OurFunctionNode('exp', dest, source, node.type))
        return dest

    @visitor.when(hulk.SqrtNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        source = self.visit(node.expr, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.OurFunctionNode(
            'sqrt', dest, source, node.type))
        return dest

    @visitor.when(hulk.LogNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        base = self.visit(node.base, scope.create_child_scope())
        arg = self.visit(node.arg, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.OurFunctionNode(
            'log', dest, base, node.type, arg))
        return dest
    
    @visitor.when(hulk.PowNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.OurFunctionNode(
            'pow', dest, left, node.type, right))
        return dest

    @visitor.when(hulk.RandNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.OurFunctionNode(
            'rand', dest, "", node.type))
        return dest

    @visitor.when(hulk.ConcatNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())

        dest = self.define_internal_local(node.type)

        dest2 = self.define_internal_local(node.type)

        if (node.left.type == c.STRING_TYPE and node.right.type == c.STRING_TYPE):
            self.register_instruction(cil.OurFunctionNode(
                'concat0', dest2, left, node.type, right))
        elif (node.left.type == c.FLOAT_TYPE and node.right.type == c.STRING_TYPE):
            self.register_instruction(cil.OurFunctionNode(
                'concat1', dest2, left, node.type, right))
        elif (node.left.type == c.STRING_TYPE and node.right.type == c.FLOAT_TYPE):
            self.register_instruction(cil.OurFunctionNode(
                'concat2', dest2, left, node.type, right))
        elif (node.left.type == c.FLOAT_TYPE and node.right.type == c.FLOAT_TYPE):
            self.register_instruction(cil.OurFunctionNode(
                'concat3', dest2, left, node.type, right))

        self.register_instruction(cil.AssignNode(dest, dest2))
        return dest

    @visitor.when(hulk.ConcatSpaceNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        space = self.visit(hulk.StringNode("\" \""),
                           scope.create_child_scope())

        dest = self.define_internal_local(node.type)

        dest2 = self.define_internal_local(node.type)
        if (node.left.type == c.STRING_TYPE):
            self.register_instruction(cil.OurFunctionNode(
                'concat0', dest2, left, node.type, space))
        elif (node.left.type == c.FLOAT_TYPE):
            self.register_instruction(cil.OurFunctionNode(
                'concat1', dest2, left, node.type, space))

        dest3 = self.define_internal_local(node.type)
        if (node.right.type == c.STRING_TYPE):
            self.register_instruction(cil.OurFunctionNode(
                'concat0', dest3, dest2, node.type, right))
        elif (node.right.type == c.FLOAT_TYPE):
            self.register_instruction(cil.OurFunctionNode(
                'concat2', dest3, dest2, node.type, right))

        self.register_instruction(cil.AssignNode(dest, dest3))

        return dest

    @visitor.when(hulk.PlusNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, f"{left} + {right}"))
        return dest

    @visitor.when(hulk.MinusNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, f"{left} - {right}"))
        return dest

    @visitor.when(hulk.StarNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, f"{left} * {right}"))
        return dest

    @visitor.when(hulk.DivNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, f"{left} / {right}"))
        return dest

    @visitor.when(hulk.ModNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.OurFunctionNode(
            'mod', dest, left, c.INT_TYPE, right))
        return dest

    @visitor.when(hulk.EQNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} == {right}"))
        return dest

    @visitor.when(hulk.NENode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} != {right}"))
        return dest

    @visitor.when(hulk.NotNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        expr = self.visit(node.lex, scope.create_child_scope())
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"!{expr}"))
        return dest

    @visitor.when(hulk.AndNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} & {right}"))
        return dest

    @visitor.when(hulk.OrNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} | {right}"))
        return dest

    @visitor.when(hulk.GENode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} >= {right}"))
        return dest

    @visitor.when(hulk.GTNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} > {right}"))
        return dest

    @visitor.when(hulk.LENode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} <= {right}"))
        return dest

    @visitor.when(hulk.LTNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.AssignNode(dest, f"{left} < {right}"))
        return dest

    @visitor.when(hulk.IfNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        dest = self.define_internal_local(node.type)

        condition = self.visit(node.condition, scope.create_child_scope())

        elif_conditions = []
        for i in range(len(node.elif_conditions)):
            elif_conditions.append(self.visit(
                node.elif_conditions[i], scope.create_child_scope()))

        index = len(self.instructions)
        self.register_instruction(cil.GotoNode(
            f'my_begin_{self.current_function.name}_{index}'))

        self.register_instruction(cil.LabelNode(
            f'my_if_{self.current_function.name}_{index}'))
        expr = self.visit(node.body, scope.create_child_scope())
        self.register_instruction(cil.AssignNode(dest, expr))

        self.register_instruction(cil.GotoNode(
            f'my_end_{self.current_function.name}_{index}'))

        for i in range(len(node.elif_conditions)):
            self.register_instruction(cil.LabelNode(
                f'my_elif_{i}_{self.current_function.name}_{index}'))
            expr = self.visit(node.elif_body[i], scope.create_child_scope())
            self.register_instruction(cil.AssignNode(dest, expr))
            self.register_instruction(cil.GotoNode(
                f'my_end_{self.current_function.name}_{index}'))

        self.register_instruction(cil.LabelNode(
            f'my_else_{self.current_function.name}_{index}'))
        else_expr = self.visit(node.else_body, scope.create_child_scope())
        self.register_instruction(cil.AssignNode(dest, else_expr))
        self.register_instruction(cil.GotoNode(
            f'my_end_{self.current_function.name}_{index}'))

        self.register_instruction(cil.LabelNode(
            f'my_begin_{self.current_function.name}_{index}'))
        self.register_instruction(
            cil.GotoIfNode(condition, f'my_if_{self.current_function.name}_{index}', f'my_else_{self.current_function.name}_{index}', elif_conditions, [f'my_elif_{i}_{self.current_function.name}_{index} 'for i in range(len(node.elif_conditions))]))
        self.register_instruction(cil.LabelNode(
            f'my_end_{self.current_function.name}_{index}'))

        return dest

    @visitor.when(hulk.DestructNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        expr = self.visit(node.expr, scope.create_child_scope())

        child = node.id.child
        func = ''
        if (child):
            if node.id.name == 'self':
                x = child.name
                func = 'self->' + x
            else:
                var = node.id.name
                stop = False
                while (not stop):
                    var, stop = scope.get_variable_info(var)
            self.register_instruction(cil.AssignNode(func, expr))

        else:

            func = node.id.name
            stop = False
            while (not stop):
                func, stop = scope.get_variable_info(func)
                self.register_instruction(cil.AssignNode(func, expr))

        return expr

    @visitor.when(hulk.AssignNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        x = self.visit(node.id, scope.create_child_scope())
        expr = self.visit(node.expr, scope.create_child_scope())
        self.register_instruction(cil.AssignNode(x, expr))
        return expr

    @visitor.when(hulk.WhileNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        dest = self.define_internal_local(node.type)

        index = len(self.instructions)
        self.register_instruction(cil.GotoNode(
            f'while_label_{self.current_function.name}_{index}'))
        self.register_instruction(cil.LabelNode(
            f'body_{self.current_function.name}_{index}'))
        expr = self.visit(node.body, scope.create_child_scope())
        self.register_instruction(cil.AssignNode(dest, expr))
        self.register_instruction(cil.LabelNode(
            f'while_label_{self.current_function.name}_{index}'))
        condition = self.visit(node.condition, scope.create_child_scope())
        self.register_instruction(cil.GotoIfNode(
            condition, f'body_{self.current_function.name}_{index}', f'endwhile_label_{self.current_function.name}_{index}'))
        self.register_instruction(cil.LabelNode(
            f'endwhile_label_{self.current_function.name}_{index}'))

        return dest

    @visitor.when(hulk.NumberNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        source = node.lex
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, source))
        return dest

    @visitor.when(hulk.BoolNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        source = node.lex
        dest = self.define_internal_local(c.INT_TYPE)
        self.register_instruction(cil.AssignNode(
            dest, 1 if source == "true" else "false"))
        return dest

    @visitor.when(hulk.BoolNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        source = node.lex
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(
            dest, 1 if source == 'true' else 0))
        return dest

    @visitor.when(hulk.StringNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)
        node.type = node.type if node.type != hulk.STRING_TYPE else 'char*'
        source = node.lex
        msg = self.register_data(source)
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.LoadNode(dest, msg))
        # self.register_instruction(cil.AssignNode(dest, source))
        return dest

    @visitor.when(hulk.BlockNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        for i in node.body:
            name = self.visit(i, scope)

        return name

    @visitor.when(hulk.LetNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        scope = scope.create_child_scope()

        self.register_instruction(cil.OpenScope())

        for arg in scope.parent.parent.local_vars:
            name = arg.name

            breakx = True
            for x in scope.parent.parent.dict.keys():
                if scope.parent.parent.dict[x] == name:
                    breakx = False
            if breakx:
                continue

            dest = self.define_internal_local(arg.type)
            scope.dict[name] = dest
            scope.define_variable(name, update_types(arg.type))
            self.register_instruction(cil.AssignNode(dest, name))

        for child in node.args:
            dest = self.visit(child.expr, scope.create_child_scope())
            scope.dict[child.id.name] = dest
            scope.define_variable(child.id.name, update_types(child.type))

            # dest2 = self.define_internal_local(update_types(child.type))
            # scope.dict[dest] = dest2
            # scope.define_variable(dest, update_types(child.type))
            # self.register_instruction(cil.AssignNode(dest2, dest))

        dest = self.visit(node.body, scope.create_child_scope())

        self.register_instruction(cil.CloseScope())

        return dest

    @visitor.when(hulk.IdentifierNode)
    def visit(self, node, scope):
        node.type = update_types(node.type)

        child = node.child

        func = ''
        if (child):
            if node.name == 'self':
                x = self.visit(child, scope.create_child_scope())
                func = 'self->' + x
            else:
                var = node.name
                stop = False
                while (not stop):
                    var, stop = scope.get_variable_info(var)

                func = self.to_function_name_in_type(
                    child.name, node.type[:-1])
                node.type = update_types(child.type)  # !!!!!!!!!!!!!!!111
                func += '(' + ", ".join(child.args) + \
                    (', ' if len(child.args) else '') + f'{var})'
        else:

            func = node.name
            stop = False
            while (not stop):
                func, stop = scope.get_variable_info(func)

        return func

    # @visitor.when(hulk.CallNode)
    # def visit(self, node, scope):
    #     node.type = update_types(node.type)

    #     params = []
    #     for child in node.args:
    #         params.append(self.visit(child, scope.create_child_scope()))

        temp = f'{self.context2[node.name]}(' + ", ".join(child for child in params) + ")"
        dest = self.define_internal_local(node.type)
        self.register_instruction(cil.AssignNode(dest, temp))

    #     return dest
