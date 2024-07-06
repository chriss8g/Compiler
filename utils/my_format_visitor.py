import utils.visitor as visitor
from nodes_types import hulk_types as hulk
import cil

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
        params_base = '\t' * (tabs+1) + 'Params BaseType' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.base_params)
        return f'{ans}\n{params}\n{params_base}\n{body}'

    @visitor.when(hulk.TypeBodyDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__TypeBodyNode'
        attributes = '\t' * (tabs+1) + 'Atributes' + '\n' + '\n'.join(self.visit(attr, tabs + 2) for attr in node.attributes)
        methods = '\t' * (tabs+1) + 'Methods' + '\n' + '\n'.join(self.visit(method, tabs + 2) for method in node.methods)
        return f'{ans}\n{attributes}\n{methods}'
    
    @visitor.when(hulk.AttributeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AttributeNode id = <expr>'
        idx = self.visit(node.name, tabs+1)
        value = self.visit(node.value, tabs + 1)
        return f'{ans}\n{idx}\n{value}'

    @visitor.when(hulk.MethodNode)
    def visit(self, node, tabs=0):
        params = ', '.join(f'({param[0],param[1]})' for param in node.params)
        ans = '\t' * tabs + f'\\__MethodNode: function {node.name} : {node.type} => <body>'
        params = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.params)
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{params}\n{body}'
    
    @visitor.when(hulk.AssignNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AssignNode:'
        id = self.visit(node.id, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{id}\n{expr}'
    
    # **************************************************
    # ************     Dentro de MAIN     **************
    # **************************************************

    @visitor.when(hulk.PrintNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__PrintNode [<sentence>]'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'
    
    @visitor.when(hulk.BlockNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__BlockNode [<expression>]'
        body = None
        if node.body is not None:
            # print(node.body)
            body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'
    
    @visitor.when(hulk.LetNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__LetNode [<expression>]'
        args = '\n'.join(self.visit(child, tabs + 1) for child in node.args)
        body = self.visit(node.body, tabs + 1)
        return f'{ans}\n{args}\n{body}'
    
    @visitor.when(hulk.WhileNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__WhileNode [<expression>]'
        condition = '\t' * (tabs+1) + '\\_ Condition' + '\n' + self.visit(node.condition, tabs + 2)
        body = '\t' * (tabs+1) + '\\_ Body' + '\n' + self.visit(node.body, tabs+2)
        return f'{ans}\n{condition}\n{body}'
    
    @visitor.when(hulk.ForRangeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ForRangeNode: {node.id.name} in range(<expr>, <expr>)  [<expression>]'
        init = '\t' * (tabs+1) + '\\_Init' + '\n' + self.visit(node.init, tabs + 2)
        final = '\t' * (tabs+1) + '\\Final' + '\n' + self.visit(node.final, tabs + 2)
        body = '\t' * (tabs+1) + '\\_ Body' + '\n' + self.visit(node.body, tabs+2)
        return f'{ans}\n{init}\n{final}\n{body}'
    
    @visitor.when(hulk.IfNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__IfNode  [<expression>]'
        print(node.condition)
        condition = '\t' * (tabs+1) + '\\_ Condition' + '\n' + self.visit(node.condition, tabs + 2)
        body = '\t' * (tabs+1) + '\\_ Body' + '\n' + self.visit(node.body, tabs+2)
        
        elifs = ''
        if node.elif_conditions:
            for i in range(len(node.elif_conditions)):
                elifs_condition = '\t' * (tabs+1) + f'\\_ Elif Condition {i}' + '\n' + self.visit(node.elif_conditions[i], tabs + 2)
                elif_body = '\t' * (tabs+1) + f'\\_ Elif Body {i}' + '\n' + self.visit(node.elif_body[i], tabs + 2)
                elifs += elifs_condition + '\n' + elif_body + '\n'
        else_body = '\t' * (tabs+1) + '\\_ Else Body' + '\n' + self.visit(node.else_body, tabs + 2)
        return f'{ans}\n{condition}\n{body}\n{elifs}{else_body}'

    @visitor.when(hulk.DestructNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\DestructNode   [<expression>]'
        id = self.visit(node.id, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{id}\n{expr}'
    
    @visitor.when(hulk.CallNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__CallNode function {node.id}   [<expression>]'
        args = '\t' * (tabs+1) + '\\_ Arguments' + '\n' + '\n'.join(self.visit(arg, tabs + 2) for arg in node.args)
        return f'{ans}\n{args}'
    
    @visitor.when(hulk.NumberNode)
    def visit(self, node, tabs=0):
        return ""
    
    @visitor.when(hulk.EQNode)
    def visit(self, node, tabs=0):
        return ""
    
    @visitor.when(hulk.GENode)
    def visit(self, node, tabs=0):
        return ""
    

    # **********************************************************
    # *******************    Operaciones  **********************
    # **********************************************************

    @visitor.when(hulk.BinaryNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__{node.__class__.__name__} [<expression>]'
        left = self.visit(node.left, tabs + 1)
        right = self.visit(node.right, tabs + 1)
        return f'{ans}\n{left}\n{right}'

    @visitor.when(hulk.AtomicNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__{node.__class__.__name__}: {node.lex}'

    @visitor.when(hulk.IdentifierNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__IdentifierNode: {node.name}'
        child = ''
        if node.child is not None:
            child = '\n' + self.visit(node.child,tabs+1)
        return f'{ans}{child}'
    
    @visitor.when(hulk.ObjectCreationNode)
    def visit(self, node, tabs=0):
        return ""
    
    


    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    
    @visitor.when(cil.TypeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__TypeNode: type {node.name}\n'
        ans = ans + '\t' * tabs + f'\t\\__TypeBodyNode'
        attributes = '\t' * (tabs+2) + 'Atributes' + '\n' + '\n'.join(self.visit(attr, tabs + 2) for attr in node.attributes)
        methods = '\t' * (tabs+2) + 'Methods' + '\n' + '\n'.join(self.visit(method, tabs + 2) for method in node.methods)
        return f'{ans}\n{attributes}\n{methods}'

    @visitor.when(cil.AllocateNode)
    def visit(self, node, tabs=0):
        return f'{'\t' * tabs}\\CallNode {node.dest} = ALOCATE {node.type.name}'
    
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
    
    @visitor.when(cil.ParamNode)
    def visit(self, node, tabs=0):
        return f'{'\t' * tabs}\\__ParamNode {node.name}'
    
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
    
