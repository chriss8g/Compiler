import utils.visitor as visitor
from nodes_types import hulk_types as hulk

class FormatVisitor(object):
    @visitor.on('node')
    def visit(self, node, tabs):
        pass

    @visitor.when(hulk.ProgramNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + '\\__ProgramNode [<program>]'
        statements = '\n'.join(self.visit(child, tabs + 1) for child in node.statements)
        main = self.visit(node.main,tabs+1)
        return f'{ans}\n{statements}\n{main}'
    
    
    # **************************************************
    # ************     Statements     **************
    # **************************************************

    
    @visitor.when(hulk.FuncDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__FuncDeclarationNode: function {node.name} : {node.type} => <body> [<statement>]'
        body = self.visit(node.body, tabs + 1)
        params = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.params)
        return f'{ans}\n{params}\n{body}'
    
    @visitor.when(hulk.TypeDeclarationNode)
    def visit(self, node, tabs=0):
        inherits = node.base_type
        ans = '\t' * tabs + f'\\__TypeNode: type {node.name} inherits {inherits} [<statement>]'
        body = self.visit(node.body, tabs + 1)
        params = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.params)
        params_base = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.base_params)
        return f'{ans}\n{params}\n{params_base}\n{body}'

    @visitor.when(hulk.TypeBodyDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__TypeBodyNode'
        attributes = '\t' * (tabs+1) + 'Atributes' + '\n' + '\n'.join(self.visit(attr, tabs + 2) for attr in node.attributes)
        methods = '\t' * (tabs+1) + 'Methods' + '\n'.join(self.visit(method, tabs + 2) for method in node.methods)
        return f'{ans}\n{attributes}\n{methods}'
    
    @visitor.when(hulk.AttributeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AttributeNode: {node.name} : {node.type} = <expr>'
        value = self.visit(node.value, tabs + 1)
        return f'{ans}\n{value}'

    @visitor.when(hulk.MethodNode)
    def visit(self, node, tabs=0):
        params = ', '.join(f'({param[0],param[1]})' for param in node.parameters)
        ans = '\t' * tabs + f'\\__MethodNode: function {node.name} : {node.type} => <body>'
        params = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.params)
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{params}\n{body}'
    
    @visitor.when(hulk.AsignNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AsignNode:'
        id = self.visit(node.id, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{id}\n{expr}'
    
    # **************************************************
    # ************     Dentro de MAIN     **************
    # **************************************************

    @visitor.when(hulk.PrintNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__PrintNode: [<sentence>]'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'
    
    @visitor.when(hulk.BlockNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__BlockNode: [<expression>]'
        body = None
        if node.body is not None:
            body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'
    
    @visitor.when(hulk.LetNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__LetNode: let [<expression>]'
        for i in range(len(node.args)):
            ans += f'{node.args[i].id} = <expr>,'
        ans += f' in <expr>'
        values = '\n'.join(self.visit(child, tabs + 1) for child in node.args)
        if(isinstance(node.body, list)):
            expr = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        else:
            expr = self.visit(node.body, tabs + 1)
        return f'{ans}\n{values}\n{expr}'


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
    
