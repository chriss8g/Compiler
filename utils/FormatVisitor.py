import utils.visitor as visitor
from nodes_types import hulk
import cil

class FormatVisitor(object):
    @visitor.on('node')
    def visit(self, node, tabs):
        pass

    @visitor.when(hulk.ProgramNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + '\\__ProgramNode [<class> ... <class>]'
        statements = '\n'.join(self.visit(child, tabs + 1) for child in node.statements)
        return f'{ans}\n{statements}'

    @visitor.when(hulk.VarDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__VarDeclarationNode: let '
        for i in range(len(node.args)):
            ans += f'{node.args[i].id} = <expr>,'
        ans += f' in <expr>'
        values = '\n'.join(self.visit(child, tabs + 1) for child in node.args)
        if(isinstance(node.body, list)):
            expr = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        else:
            expr = self.visit(node.body, tabs + 1)
        return f'{ans}\n{values}\n{expr}'

    @visitor.when(hulk.FuncDeclarationNode)
    def visit(self, node, tabs=0):
        params = ', '.join(f'{param}' for param in node.params)
        ans = '\t' * tabs + f'\\__FuncDeclarationNode: function {node.id} : {node.type} => <body>'
        if isinstance(node.body, list):
            body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        else:
            body = self.visit(node.body, tabs + 1)
        params_info = '\n'.join('\t' * (tabs + 1) + f'Param {i+1}: {param}' for i, param in enumerate(node.params))
        return f'{ans}\n{params_info}\n{body}'

    @visitor.when(hulk.BinaryNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__<expr> {node.__class__.__name__} <expr>'
        left = self.visit(node.left, tabs + 1)
        right = self.visit(node.right, tabs + 1)
        return f'{ans}\n{left}\n{right}'

    @visitor.when(hulk.AtomicNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__ {node.__class__.__name__}: {node.lex}'

    @visitor.when(hulk.CallNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__CallNode: {node.id}(<expr>, ..., <expr>)'
        args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.args)
        return f'{ans}\n{args}'

    @visitor.when(hulk.PrintNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__PrintNode <expr>'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(hulk.WhileNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__WhileNode'
        condition = self.visit(node.condition, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)

        return f'{ans}\n{condition}\n{expr}'

    @visitor.when(hulk.ForNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ForNode: {node.id} in <expr>'
        iterable = self.visit(node.iterable, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{iterable}\n{expr}'

    @visitor.when(hulk.ForRangeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ForRangeNode: {node.id} in range(<expr>, <expr>)'
        init = self.visit(node.init, tabs + 1)
        final = self.visit(node.final, tabs + 1)
        body = self.visit(node.body, tabs + 1)
        return f'{ans}\n{init}\n{final}\n{body}'

    @visitor.when(hulk.IfNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__IfNode: if <expr>'
        condition = self.visit(node.condition, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        else_expr = self.visit(node.else_expr, tabs + 1)
        elif_conditions = '\n'.join(self.visit(cond, tabs + 1) for cond in node.elif_conditions)
        elif_expr = '\n'.join(self.visit(ex, tabs + 1) for ex in node.elif_expr)
        return f'{ans}\n{condition}\n{expr}' + '\n' + '\t' * tabs + f'\\__Elif <expr>:' + f'\n{elif_conditions}\n{elif_expr}' + '\n' + '\t' * tabs + f'\\__Else:' + f'\n{else_expr}'

    @visitor.when(hulk.BlockNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__BlockNode'
        body = None
        if node.body is not None:
            body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'

    @visitor.when(hulk.AsignNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AsignNode: {node.id.lex} := <expr>'
        id = self.visit(node.id, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{id}\n{expr}'
    
    @visitor.when(hulk.DestructNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\DestructNode: {node.id.lex} := <expr>'
        id = self.visit(node.id, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{id}\n{expr}'

    @visitor.when(hulk.SinNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__SinNode: sin(<expr>)'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(hulk.CosNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__CosNode: cos(<expr>)'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(hulk.SqrtNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__SqrtNode: sqrt(<expr>)'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(hulk.ExpNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ExpNode: exp(<expr>)'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(hulk.LogNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__LogNode: log(<expr>)'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(hulk.RandNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__RandNode'
        return ans

    @visitor.when(hulk.ConstantNumNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__ConstantNumNode: {node.lex}'

    @visitor.when(hulk.BoolNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__BoolNode: {node.lex}'

    @visitor.when(hulk.StringNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__StringNode: {node.lex}'

    @visitor.when(hulk.VariableNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__VariableNode: {node.lex}'

    @visitor.when(hulk.TypeNode)
    def visit(self, node, tabs=0):
        inherits = node.base_type
        ans = '\t' * tabs + f'\\__TypeNode: {node.name},  Inherits from: {inherits}'
        body = self.visit(node.body, tabs + 1)
        params_str = ', '.join([f'{param}' for param in node.params])
        params_info = '\n'.join('\t' * (tabs + 1) + f'Param {i+1}: {param}' for i, param in enumerate(node.params))
        return f'{ans}\n{params_info}\n{body}'

    @visitor.when(hulk.TypeBodyNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__TypeBodyNode'
        attributes = '\n'.join(self.visit(attr, tabs + 1) for attr in node.attributes)
        methods = '\n'.join(self.visit(method, tabs + 1) for method in node.methods)
        return f'{ans}\n{attributes}\n{methods}'

    @visitor.when(hulk.AttributeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AttributeNode: {node.name} = <expr>'
        value = self.visit(node.value, tabs + 1)
        return f'{ans}\n{value}'

    @visitor.when(hulk.MethodNode)
    def visit(self, node, tabs=0):
        params = ', '.join(f'({param[0],param[1]})' for param in node.parameters)
        ans = '\t' * tabs + f'\\__MethodNode: function {node.name}({params}) : {node.type} => <body>'
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'

    @visitor.when(hulk.ObjectCreationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ObjectCreationNode: new {node.type_name}(<expr>, ..., <expr>)'
        args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.arguments)
        return f'{ans}\n{args}'

    @visitor.when(hulk.MethodCallNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__MethodCallNode: {node.object_name}.{node.method_name}(<expr>, ..., <expr>)'
        args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.arguments)
        return f'{ans}\n{args}'



    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    
    # @visitor.when(cil.IfNode)
    # def visit(self, node, tabs=0):
    #     ans = '\t' * tabs + f'\\__IfNode:\n {'\t' * (tabs+1)}\\__condition {node.condition} \n' + '\t' * (tabs+1) 
    #     # condition = self.visit(node.condition, tabs + 1)
    #     # elif_conditions = '\n'.join(self.visit(cond, tabs + 1) for cond in node.elif_conditions)
    #     # elif_expr = '\n'.join(self.visit(ex, tabs + 1) for ex in node.elif_expr)
    #     # return f'{ans}\n{condition}\n{expr}' + '\n' + '\t' * tabs + f'\\__Elif <expr>:' + f'\n{elif_conditions}\n{elif_expr}' + '\n' + '\t' * tabs + f'\\__Else:' + f'\n{else_expr}'
    #     return f'{ans}\\body: call {node.expr}' + '\n' + '\t' * (tabs+1) + f'\\__else_body: ' + f'call {node.else_expr}'
        
    @visitor.when(cil.PrintNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__PrintNode {node.expr}'
        return f'{ans}'
    
    @visitor.when(cil.ProgramNode)
    def visit(self, node, tabs=0):
        dottypes = '\\__.TYPES\n' + f'{'\t' * tabs} \n'.join(self.visit(t, tabs + 1) for t in node.dottypes)
        dotdata = '\\__.DATA\n' + f'{'\t' * tabs} \n'.join(self.visit(t, tabs + 1) for t in node.dotdata)
        dotcode = '\\__.CODE\n' + f'{'\t' * tabs} \n'.join(self.visit(t, tabs + 1) for t in node.dotcode)

        return f'{dottypes}\n{dotdata}\n{dotcode}'
    
    @visitor.when(cil.FunctionNode)
    def visit(self, node, tabs=0):
        params = f'{'\t' * tabs}\t \\__params\n' + '\n'.join(self.visit(x, tabs + 2) for x in node.params)
        localvars = f'{'\t' * tabs}\t \\__local_vars\n' +  '\n'.join(self.visit(x, tabs + 2) for x in node.localvars)
        instructions = f'{'\t' * tabs}\t \\__instructions\n' +  '\n'.join(self.visit(x, tabs + 2) for x in node.instructions)

        return f'{'\t' * tabs} \\__FunctionNode function <{node.name}>\n{params}\n{localvars}\n{instructions}'
    
    @visitor.when(cil.StaticCallNode)
    def visit(self, node, tabs=0):
        return f'{'\t' * tabs}\\CallNode {node.dest} = call {node.function}'
    
    @visitor.when(cil.ReturnNode)
    def visit(self, node, tabs=0):
        return f'{'\t' * tabs}\\__ReturnNode return {node.value if node.value is not None else ""}'
    
    @visitor.when(cil.LocalNode)
    def visit(self, node, tabs=0):
        return f'{'\t' * tabs}\\__LocalNode {node.name}'
    
    @visitor.when(cil.LabelNode)
    def visit(self, node, tabs=0):
        return f'{'\t' * tabs}\\__LabelNode {node.label}'
    
    @visitor.when(cil.GotoNode)
    def visit(self, node, tabs=0):
        return f'{'\t' * tabs}\\GotoNode {node.label}'
    
    @visitor.when(cil.GotoIfNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__GotoIfNode:\n {'\t' * (tabs+1)}\\__condition {node.condition} \n' + '\t' * (tabs+1) 
        return f'{ans}\\goto: {node.label}' + '\n' + '\t' * (tabs+1) + f'\\__else_goto: ' + f' {node.label_else}'
        
    
    
    # @visitor.when(cil.LogicNode)
    # def visit(self, node, tabs=0):
    #     ans = '\t' * tabs + f'\\__{node.left} {node.op} {node.right}'
    #     return f'{ans}'
    
    # @visitor.when(cil.ArithmeticNode)
    # def visit(self, node, tabs=0):
    #     ans = '\t' * tabs + f'\\__{node.left} {node.op} {node.right}'
    #     return f'{ans}'
    
    @visitor.when(cil.AssignNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AsignNode: {node.dest} = {node.source}'
        return ans
    
