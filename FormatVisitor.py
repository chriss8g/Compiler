import utils.visitor as visitor
from my_types import *

class FormatVisitor(object):
    @visitor.on('node')
    def visit(self, node, tabs):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + '\\__ProgramNode [<class> ... <class>]'
        statements = '\n'.join(self.visit(child, tabs + 1) for child in node.statements)
        return f'{ans}\n{statements}'

    @visitor.when(VarDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__VarDeclarationNode: let '
        for i in range(len(node.args)):
            ans += f'{node.args[i].id} = <expr>,'
        ans += f' in <expr>'
        values = '\n'.join(self.visit(child, tabs + 1) for child in node.args)
        expr = self.visit(node.body, tabs + 1)
        return f'{ans}\n{values}\n{expr}'

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, tabs=0):
        params = ', '.join(param.lex for param in node.params)
        ans = '\t' * tabs + f'\\__FuncDeclarationNode: function {node.id.lex}({params}) => <body>'
        if isinstance(node.body, list):
            body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        else:
            body = self.visit(node.body, tabs + 1)
        return f'{ans}\n{body}'

    @visitor.when(BinaryNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__<expr> {node.__class__.__name__} <expr>'
        left = self.visit(node.left, tabs + 1)
        right = self.visit(node.right, tabs + 1)
        return f'{ans}\n{left}\n{right}'

    @visitor.when(AtomicNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__ {node.__class__.__name__}: {node.lex}'

    @visitor.when(CallNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__CallNode: {node.id}(<expr>, ..., <expr>)'
        args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.args)
        return f'{ans}\n{args}'

    @visitor.when(PrintNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__PrintNode <expr>'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(WhileNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__WhileNode'
        condition = self.visit(node.condition, tabs + 1)
        expr = '\n'.join(self.visit(ex, tabs + 1) for ex in node.expr)

        return f'{ans}\n{condition}\n{expr}'

    @visitor.when(ForNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ForNode: {node.id} in <expr>'
        iterable = self.visit(node.iterable, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{iterable}\n{expr}'

    @visitor.when(ForRangeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ForRangeNode: {node.id} in range(<expr>, <expr>)'
        init = self.visit(node.init, tabs + 1)
        final = self.visit(node.final, tabs + 1)
        body = self.visit(node.body, tabs + 1)
        return f'{ans}\n{init}\n{final}\n{body}'

    @visitor.when(IfNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__IfNode: if <expr>'
        condition = self.visit(node.condition, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        else_expr = self.visit(node.else_expr, tabs + 1)
        elif_conditions = '\n'.join(self.visit(cond, tabs + 1) for cond in node.elif_conditions)
        elif_expr = '\n'.join(self.visit(ex, tabs + 1) for ex in node.elif_expr)
        return f'{ans}\n{condition}\n{expr}\nelse\n{else_expr}\nelif\n{elif_conditions}\n{elif_expr}'

    @visitor.when(BlockNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__BlockNode'
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'

    @visitor.when(AsignNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AsignNode: {node.id.lex} := <expr>'
        id = self.visit(node.id, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{id}\n{expr}'

    @visitor.when(SinNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__SinNode: sin(<expr>)'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(CosNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__CosNode: cos(<expr>)'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(SqrtNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__SqrtNode: sqrt(<expr>)'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(ExpNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ExpNode: exp(<expr>)'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(LogNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__LogNode: log(<expr>)'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(RandNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__RandNode'
        return ans

    @visitor.when(ConstantNumNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__ConstantNumNode: {node.lex}'

    @visitor.when(BoolNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__BoolNode: {node.lex}'

    @visitor.when(StringNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__StringNode: {node.lex}'

    @visitor.when(VariableNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__VariableNode: {node.lex}'

    @visitor.when(TypeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__TypeNode: {node.name}'
        body = self.visit(node.body, tabs + 1)
        if node.base_type:
            base_type = self.visit(node.base_type, tabs + 1)
            return f'{ans}\n{body}\n{base_type}'
        return f'{ans}\n{body}'

    @visitor.when(TypeBodyNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__TypeBodyNode'
        attributes = '\n'.join(self.visit(attr, tabs + 1) for attr in node.attributes)
        methods = '\n'.join(self.visit(method, tabs + 1) for method in node.methods)
        return f'{ans}\n{attributes}\n{methods}'

    @visitor.when(AttributeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AttributeNode: {node.name} = <expr>'
        value = self.visit(node.value, tabs + 1)
        return f'{ans}\n{value}'

    @visitor.when(MethodNode)
    def visit(self, node, tabs=0):
        params = ', '.join(param.lex for param in node.parameters)
        ans = '\t' * tabs + f'\\__MethodNode: function {node.name}({params}) => <body>'
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'

    @visitor.when(ObjectCreationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ObjectCreationNode: new {node.type_name}(<expr>, ..., <expr>)'
        args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.arguments)
        return f'{ans}\n{args}'

    @visitor.when(MethodCallNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__MethodCallNode: {node.object_name}.{node.method_name}(<expr>, ..., <expr>)'
        args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.arguments)
        return f'{ans}\n{args}'

