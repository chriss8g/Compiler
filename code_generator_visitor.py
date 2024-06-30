import cmp.visitor as visitor
from my_types import *
from scope import Scope

class CodeGeneratorVisitor(object):

    def __init__(self):
        self.temp_count = 0
        self.headers = []

    @visitor.on('node')
    def visit(self, node, scope):
        pass
    
    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        scope = Scope() if not scope else scope
        body = "int main() {\n"
        statements = '\n    '.join(self.visit(child, scope.create_child_scope()) for child in node.statements)
        return ''.join(self.headers) + f'{body}\n{statements}\n    return 0;\n}}\n'
    
    @visitor.when(VarDeclarationNode)
    def visit(self, node, scope=None):
        ans = "{\n"
        for i in range(len(node.ids)):
            scope.define_variable(node.ids[i])
            ans += f'int {node.ids[i]} = {self.visit(node.exprs[i], scope.create_child_scope())};'

        expr = self.visit(node.body, scope.create_child_scope())

        return f'{ans}\n{expr}}}'
    
    
    # @visitor.when(FuncDeclarationNode)
    # def visit(self, node, tabs=0):
    #     params = ', '.join(param for param in node.params)
    #     ans = '\t' * tabs + f'\\__FuncDeclarationNode: function {node.id}({params}) => <body>'
    #     if( isinstance(node.body, list)):
    #         body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
    #     else:
    #         body = self.visit(node.body, tabs + 1)
    #     return f'{ans}\n{body}'

    @visitor.when(PlusNode)
    def visit(self, node, scope=None):
        ans = "+"
        left = self.visit(node.left, scope.create_child_scope())
        right = self.visit(node.right, scope.create_child_scope())
        return f'{left} {ans} {right}'

    @visitor.when(AtomicNode)
    def visit(self, node, scope=None):
        return f'{node.lex}'
    
    # @visitor.when(CallNode)
    # def visit(self, node, tabs=0):
    #     ans = '\t' * tabs + f'\\__CallNode: {node.id}(<expr>, ..., <expr>)'
    #     args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.args)
    #     return f'{ans}\n{args}'
    
    @visitor.when(PrintNode)
    def visit(self, node, scope=None):
        self._add_header("#include <stdio.h>\n")
        ans = 'printf("%d\\n",'
        expr = self.visit(node.expr, scope.create_child_scope())
        return f'{ans} {expr} );'
    

    def _add_header(self, header):
        if header not in self.headers:
            self.headers.append(header)

    def new_temp(self):
        self.temp_count += 1
        return f"temp_{self.temp_count}"