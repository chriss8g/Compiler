import utils.visitor as visitor
from nodes_types.hulk_types import *

class FormatVisitor(object):
    @visitor.on('node')
    def visit(self, node, tabs):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + '\\__ProgramNode [<program>]'
        statements = '\n'.join(self.visit(child, tabs + 1) for child in node.statements)
        main = self.visit(node.main,tabs+1)
        return f'{ans}\n{statements}\n{main}'
    
    
    # **************************************************
    # ************     Statements     **************
    # **************************************************

    
    @visitor.when(FuncDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__FuncDeclarationNode: function {node.name} : {node.type} => <body> [<statement>]'
        body = self.visit(node.body, tabs + 1)
        params = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.params)
        return f'{ans}\n{params}\n{body}'
    
    @visitor.when(TypeDeclarationNode)
    def visit(self, node, tabs=0):
        inherits = node.base_type
        ans = '\t' * tabs + f'\\__TypeNode: type {node.name} inherits {inherits} [<statement>]'
        body = self.visit(node.body, tabs + 1)
        params = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.params)
        params_base = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.base_params)
        return f'{ans}\n{params}\n{params_base}\n{body}'

    @visitor.when(TypeBodyDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__TypeBodyNode'
        attributes = '\t' * (tabs+1) + 'Atributes' + '\n' + '\n'.join(self.visit(attr, tabs + 2) for attr in node.attributes)
        methods = '\t' * (tabs+1) + 'Methods' + '\n'.join(self.visit(method, tabs + 2) for method in node.methods)
        return f'{ans}\n{attributes}\n{methods}'
    
    @visitor.when(AttributeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AttributeNode: {node.name} : {node.type} = <expr>'
        value = self.visit(node.value, tabs + 1)
        return f'{ans}\n{value}'

    @visitor.when(MethodNode)
    def visit(self, node, tabs=0):
        params = ', '.join(f'({param[0],param[1]})' for param in node.parameters)
        ans = '\t' * tabs + f'\\__MethodNode: function {node.name} : {node.type} => <body>'
        params = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.params)
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{params}\n{body}'
    
    @visitor.when(AsignNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AsignNode:'
        id = self.visit(node.id, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{id}\n{expr}'
    
    # **************************************************
    # ************     Dentro de MAIN     **************
    # **************************************************

    @visitor.when(PrintNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__PrintNode: [<sentence>]'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'
    
    @visitor.when(BlockNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__BlockNode: [<expression>]'
        body = None
        if node.body is not None:
            body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'
    
    @visitor.when(LetNode)
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
