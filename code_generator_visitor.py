import cmp.visitor as visitor
from nodes_types.hulk import *
from semantic_checker.scope import Scope
import cil

class CodeGeneratorVisitor(object):

    def __init__(self):
        self.headers = []

    @visitor.on('node')
    def visit(self, node, scope=None):
        pass

    @visitor.when(cil.ProgramNode)
    def visit(self, node, scope):

        scope = Scope() if not scope else scope
    
        dottypes = ''#'\\__.TYPES\n' + f'{'\t' * tabs} \n'.join(self.visit(t, tabs + 1) for t in node.dottypes)
        
        dotdata = ''
        for t in node.dotdata:
            dotdata = dotdata + '#DEFINE' + self.visit(t, scope.create_child_scope()) + "\n"

        dotcode = ""
        dotcode = dotcode + '\n    '.join(self.visit(child, scope.create_child_scope()) for child in node.dotcode)

        return f'{"\n".join(self.headers)}' + f'{dottypes}\n{dotdata}\n{dotcode}'

    @visitor.when(cil.IfNode)
    def visit(self, node, scope):
        ans = f'if( {node.condition}) \n\t{node.expr}();\n else \n\t{node.else_expr}();\n'
        # condition = self.visit(node.condition, tabs + 1)
        # elif_conditions = '\n'.join(self.visit(cond, tabs + 1) for cond in node.elif_conditions)
        # elif_expr = '\n'.join(self.visit(ex, tabs + 1) for ex in node.elif_expr)
        # return f'{ans}\n{condition}\n{expr}' + '\n' + '\t' * tabs + f'\\__Elif <expr>:' + f'\n{elif_conditions}\n{elif_expr}' + '\n' + '\t' * tabs + f'\\__Else:' + f'\n{else_expr}'
        return f'{ans}'
        
    @visitor.when(cil.PrintNode)
    def visit(self, node, scope):

        header = "#include <stdio.h>"
        if(header not in self.headers):
            self.headers.append(header)

        ans = f'printf("%d\\n", {node.expr});\n'
        return f'{ans}'
    
    
    @visitor.when(cil.FunctionNode)
    def visit(self, node, scope):
        params = ', '.join(self.visit(x, scope.create_child_scope()) for x in node.params)

        localvars = ""
        for x in node.localvars:
            localvars = localvars + self.visit(x, scope.create_child_scope()) + ";\n"

        instructions = ""
        for x in node.instructions:
            instructions = instructions + self.visit(x, scope.create_child_scope()) + ';\n'

        return f'int {node.name}({params}){{ \n{localvars}\n{instructions} }}'
    
    @visitor.when(cil.StaticCallNode)
    def visit(self, node, scope):
        return f'{node.dest} = {node.function}();'
    
    @visitor.when(cil.ReturnNode)
    def visit(self, node, scope):
        return f'return {node.value if node.value is not None else ""};'
    
    @visitor.when(cil.LocalNode)
    def visit(self, node, scope):
        return f'int {node.name}'
    
    @visitor.when(cil.LogicNode)
    def visit(self, node, scope):
        ans = f'{node.left} {node.op} {node.right}'
        return f'{ans}'
    
    @visitor.when(cil.AssignNode)
    def visit(self, node, scope):
        ans = f'{node.dest} = {node.source}'
        return ans
    