import cmp.visitor as visitor
from nodes_types.hulk import *
from semantic_checker.scope import Scope

class CodeGeneratorVisitor(object):

    def __init__(self):
        pass

    @visitor.on('node')
    def visit(self, node, scope):
        pass


    @visitor.when(cil.IfNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__IfNode:\n {'\t' * (tabs+1)}\\__condition {node.condition} \n' + '\t' * (tabs+1) 
        # condition = self.visit(node.condition, tabs + 1)
        # elif_conditions = '\n'.join(self.visit(cond, tabs + 1) for cond in node.elif_conditions)
        # elif_expr = '\n'.join(self.visit(ex, tabs + 1) for ex in node.elif_expr)
        # return f'{ans}\n{condition}\n{expr}' + '\n' + '\t' * tabs + f'\\__Elif <expr>:' + f'\n{elif_conditions}\n{elif_expr}' + '\n' + '\t' * tabs + f'\\__Else:' + f'\n{else_expr}'
        return f'{ans}\\body: call {node.expr}' + '\n' + '\t' * (tabs+1) + f'\\__else_body: ' + f'call {node.else_expr}'
        
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

        return f'{'\t' * tabs} \\__function <{node.name}>\n{params}\n{localvars}\n{instructions}'
    
    @visitor.when(cil.StaticCallNode)
    def visit(self, node, tabs=0):
        return f'{'\t' * tabs}\\Call {node.dest} = call {node.function}'
    
    @visitor.when(cil.ReturnNode)
    def visit(self, node, tabs=0):
        return f'{'\t' * tabs}\\__RETURN {node.value if node.value is not None else ""}'
    
    @visitor.when(cil.LocalNode)
    def visit(self, node, tabs=0):
        return f'{'\t' * tabs}\\__LocalNode {node.name}'
    
    @visitor.when(cil.LogicNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__{node.left} {node.op} {node.right}'
        return f'{ans}'
    
    @visitor.when(cil.AssignNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AsignNode: {node.dest} = {node.source}'
        return ans
    
    # @visitor.when(ProgramNode)
    # def visit(self, node, scope=None):
    #     scope = Scope() if not scope else scope
    #     body = "int main() {\n"
    #     statements = '\n    '.join(self.visit(child, scope.create_child_scope()) for child in node.statements)
    #     return ''.join(self.headers) + f'{body}\n{statements}\n    return 0;\n}}\n'
    
    # @visitor.when(VarDeclarationNode)
    # def visit(self, node, scope=None):
    #     ans = "{\n"
    #     for i in range(len(node.ids)):
    #         scope.define_variable(node.ids[i])
    #         ans += f'int {node.ids[i]} = {self.visit(node.exprs[i], scope.create_child_scope())};'

    #     expr = self.visit(node.body, scope.create_child_scope())

    #     return f'{ans}\n{expr}}}'
    
    
    # # @visitor.when(FuncDeclarationNode)
    # # def visit(self, node, tabs=0):
    # #     params = ', '.join(param for param in node.params)
    # #     ans = '\t' * tabs + f'\\__FuncDeclarationNode: function {node.id}({params}) => <body>'
    # #     if( isinstance(node.body, list)):
    # #         body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
    # #     else:
    # #         body = self.visit(node.body, tabs + 1)
    # #     return f'{ans}\n{body}'

    # @visitor.when(PlusNode)
    # def visit(self, node, scope=None):
    #     ans = "+"
    #     left = self.visit(node.left, scope.create_child_scope())
    #     right = self.visit(node.right, scope.create_child_scope())
    #     return f'{left} {ans} {right}'
    
    # @visitor.when(MinusNode)
    # def visit(self, node, scope=None):
    #     ans = "-"
    #     left = self.visit(node.left, scope.create_child_scope())
    #     right = self.visit(node.right, scope.create_child_scope())
    #     return f'{left} {ans} {right}'
    
    # @visitor.when(StarNode)
    # def visit(self, node, scope=None):
    #     ans = "*"
    #     left = self.visit(node.left, scope.create_child_scope())
    #     right = self.visit(node.right, scope.create_child_scope())
    #     return f'{left} {ans} {right}'
    
    # @visitor.when(DivNode)
    # def visit(self, node, scope=None):
    #     ans = "/"
    #     left = self.visit(node.left, scope.create_child_scope())
    #     right = self.visit(node.right, scope.create_child_scope())
    #     return f'{left} {ans} {right}'
    
    # @visitor.when(PowNode)
    # def visit(self, node, scope=None):
    #     left = self.visit(node.left, scope.create_child_scope())
    #     right = self.visit(node.right, scope.create_child_scope())

    #     self._add_header("#include <math.h>\n")
    #     return f'pow({left}, {right})'

    # @visitor.when(AtomicNode)
    # def visit(self, node, scope=None):
    #     return f'{node.lex}'
    
    # # @visitor.when(CallNode)
    # # def visit(self, node, tabs=0):
    # #     ans = '\t' * tabs + f'\\__CallNode: {node.id}(<expr>, ..., <expr>)'
    # #     args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.args)
    # #     return f'{ans}\n{args}'
    
    # @visitor.when(PrintNode)
    # def visit(self, node, scope=None):
    #     self._add_header("#include <stdio.h>\n")
    #     expr = self.visit(node.expr, scope.create_child_scope())
    #     ans = 'printf("%f\\n",' if node.expr.type == FLOAT_TYPE else 'printf("%d\\n",'
    #     return f'{ans} {expr} );'
    

    # def _add_header(self, header):
    #     if header not in self.headers:
    #         self.headers.append(header)

    # def new_temp(self):
    #     self.temp_count += 1
    #     return f"temp_{self.temp_count}"
    
