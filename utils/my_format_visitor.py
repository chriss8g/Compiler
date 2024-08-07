import utils.visitor as visitor
from nodes_types import hulk_types as hulk
import nodes_types.cil as cil

class FormatVisitor(object):
    @visitor.on('node')
    def visit(self, node, tabs):
        pass

    @visitor.when(hulk.ProgramNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + '\\__ProgramNode [<program>]'
        statements = ""
        if node.statements:
            statements = '\n' + '\n'.join(self.visit(child, tabs + 1) for child in node.statements)
        main = self.visit(node.main,tabs+1)
        return f'{ans}{statements}\n{main}'
    
    
    # **************************************************
    # ************     Statements     **************
    # **************************************************

    @visitor.when(hulk.ProtocolNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ProtocolNode protocol {node.name} : {node.extension} at line {node.line}   [<statement>]'
        body = ''
        if node.body:
            body = '\t' * (tabs+1) + '\\__Body' + '\n' + '\n'.join(self.visit(child, tabs+2) for child in node.body)
        return f'{ans}\n{body}'
    
    @visitor.when(hulk.MethodProtocolNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__MethodProtocolNode {node.name} : {node.type}  at line {node.line}   [<statement>]'
        args = ''
        if node.args:
            args = '\t' * (tabs+1) + 'Arguments' + '\n' + '\n'.join('\t' * (tabs+2) + f'{arg}' for arg in node.args)
        return f'{ans}\n{args}'
    
    
    @visitor.when(hulk.FuncDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__FuncDeclarationNode: function {node.name} : {node.type} => <body>  at line {node.line}   [<statement>]'
        body = '\t' * (tabs+1) + 'Body' + '\n' + self.visit(node.body, tabs + 1)
        params = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+1) + f'{param}' for param in node.params)
        return f'{ans}\n{params}\n{body}'
    
    @visitor.when(hulk.TypeDeclarationNode)
    def visit(self, node, tabs=0):
        inherits = node.base_type
        ans = '\t' * tabs + f'\\__TypeNode: type {node.name} inherits {inherits}  at line {node.line}  [<statement>]'
        body = self.visit(node.body, tabs + 1)
        params = ''
        if node.params:
            params = '\n' + '\t' * (tabs+1) + '\n'.join('\t' * (tabs+2) + f'Param {i} {param}' for i,param in enumerate(node.params))
        params_base = ''
        if node.base_params:
            params_base = '\n' + '\t' * (tabs+1) + '\n'.join('\t' * (tabs+2) + f'Params BaseType {i} {param}' for i,param in enumerate(node.base_params))
        return f'{ans}{params}{params_base}\n{body}'

    @visitor.when(hulk.TypeBodyDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__TypeBodyNode   at line {node.line}  '
        attributes = '\t' * (tabs+1) + 'Atributes' + '\n' + '\n'.join(self.visit(attr, tabs + 2) for attr in node.attributes)
        methods = '\t' * (tabs+1) + 'Methods' + '\n' + '\n'.join(self.visit(method, tabs + 2) for method in node.methods)
        return f'{ans}\n{attributes}\n{methods}'
    
    @visitor.when(hulk.AttributeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AttributeNode id = <expr>   at line {node.line}  '
        idx = self.visit(node.id, tabs+1)
        value = self.visit(node.value, tabs + 1)
        return f'{ans}\n{idx}\n{value}'

    @visitor.when(hulk.MethodNode)
    def visit(self, node, tabs=0):
        params = ', '.join(f'({param[0],param[1]})' for param in node.params)
        ans = '\t' * tabs + f'\\__MethodNode: function {node.name} : {node.type} => <body>   at line {node.line}  '
        params = '\t' * (tabs+1) + 'Params' + '\n' + '\n'.join('\t' * (tabs+2) + f'{param}' for param in node.params)
        if isinstance(node.body, list):
            body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        else:
            body = self.visit(node.body, tabs + 1)

        return f'{ans}\n{params}\n{body}'
    
    @visitor.when(hulk.AssignNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AssignNode:'
        if node.type:
            ans = '\t' * tabs + f'\\__AssignNode : {node.type}   at line {node.line}  '
        id = self.visit(node.id, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{id}\n{expr}'
    
    # **************************************************
    # ************     Dentro de MAIN     **************
    # **************************************************

    @visitor.when(hulk.PrintNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__PrintNode  at line {node.line}  [<expression>]'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'
    
    @visitor.when(hulk.BlockNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__BlockNode  at line {node.line}  [<expression>]'
        body = None
        if node.body is not None:
            body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'
    
    @visitor.when(hulk.LetNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__LetNode  at line {node.line}  [<expression>]'
        args = '\n'.join(self.visit(child, tabs + 1) for child in node.args)
        body = self.visit(node.body, tabs + 1)
        return f'{ans}\n{args}\n{body}'
    
    @visitor.when(hulk.WhileNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__WhileNode  at line {node.line}  [<expression>]'
        condition = '\t' * (tabs+1) + '\\_ Condition' + '\n' + self.visit(node.condition, tabs + 2)
        body = '\t' * (tabs+1) + '\\_ Body' + '\n' + self.visit(node.body, tabs+2)
        return f'{ans}\n{condition}\n{body}'
    
    @visitor.when(hulk.ForRangeNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ForRangeNode: {node.id.name} in range(<expr>, <expr>)   at line {node.line}  [<expression>]'
        init = '\t' * (tabs+1) + '\\_Init' + '\n' + self.visit(node.init, tabs + 2)
        final = '\t' * (tabs+1) + '\\Final' + '\n' + self.visit(node.final, tabs + 2)
        body = '\t' * (tabs+1) + '\\_ Body' + '\n' + self.visit(node.body, tabs+2)
        return f'{ans}\n{init}\n{final}\n{body}'
    
    @visitor.when(hulk.IfNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__IfNode   at line {node.line}  [<expression>]'
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
        ans = '\t' * tabs + f'\\__DestructNode at line {node.line}   [<expression>]'
        id = self.visit(node.id, tabs + 1)
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{id}\n{expr}'
    
    @visitor.when(hulk.CallNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__CallNode {node.name}  at line {node.line}   [<expression>]'
        args = ''
        if node.args:
            args = '\n' + '\t' * (tabs+1) + '\\_ Arguments' + '\n' + '\n'.join(self.visit(arg, tabs + 2) for arg in node.args)
        parent = ''
        if node.parent is not None:
            parent = '\n' + self.visit(node.parent,tabs+1)
        return f'{ans}{args}{parent}'
    
    @visitor.when(hulk.IsNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__{node.__class__.__name__}  at line {node.line}  [<expression>]'
        id = self.visit(node.id, tabs + 1)
        typex = '\t' * (tabs+1) + f'\\__ Type: {node.type}'
        return f'{ans}\n{id}\n{typex}'
    
    @visitor.when(hulk.AsNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__{node.__class__.__name__}  at line {node.line}  [<expression>]'
        id = self.visit(node.id, tabs + 1)
        typex = '\t' * (tabs+1) + f'\\__ Type: {node.type}'
        return f'{ans}\n{id}\n{typex}'
        

    # **********************************************************
    # *******************    Operaciones  **********************
    # **********************************************************

    @visitor.when(hulk.BinaryNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__{node.__class__.__name__}  at line {node.line}  [<expression>]'
        left = self.visit(node.left, tabs + 1)
        right = self.visit(node.right, tabs + 1)
        return f'{ans}\n{left}\n{right}'
    
    @visitor.when(hulk.AtomicNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__{node.__class__.__name__}: {node.lex}  at line {node.line}  '
    
    @visitor.when(hulk.SingleAritmeticOpNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__{node.__class__.__name__}  at line {node.line}    [<expression>]'
        body = self.visit(node.expr,tabs+1)
        return f'{ans}\n{body}'

    @visitor.when(hulk.IdentifierNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__IdentifierNode: {node.name} : {node.type}'
        parent = ''
        if node.parent is not None:
            parent = '\n' + self.visit(node.parent,tabs+1)
        return f'{ans}{parent}'
    
    @visitor.when(hulk.ObjectCreationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\_ObjectCreationNode: new {node.type}   at line {node.line}  [<expression>]'
        args = ""
        if node.args != []:
            for arg in node.args:
                args += '\n' + self.visit(arg,tabs+1)
        return f'{ans}{args}'
    
    @visitor.when(hulk.SelfNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\SelfNode  at line {node.line}   [<expression>]'
        child = self.visit(node.lex,tabs+1)
        return f'{ans}\n{child}'

    @visitor.when(hulk.LogNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__{node.__class__.__name__}  at line {node.line}  [<expression>]'
        left = self.visit(node.base, tabs + 1)
        right = self.visit(node.arg, tabs + 1)
        return f'{ans}\n{left}\n{right}'

    @visitor.when(hulk.RandNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__{node.__class__.__name__} ()   at line {node.line}  '

    @visitor.when(hulk.VectorNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__VectorNode  at line {node.line}   [<expression>]'
        items_head = '\t' * (tabs+1) + '\\_Items'
        items_body = '\n'.join(self.visit(item,tabs+2) for item in node.items)
        return f'{ans}\n{items_head}\n{items_body}'

    @visitor.when(hulk.ForNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ForNode: {node.id.name} in <vector>  at line {node.line}   [<expression>]'
        iter_var = self.visit(node.id,tabs+1)
        iter_vect = self.visit(node.iterable,tabs+1)
        body = self.visit(node.body,tabs+1)
        return f'{ans}\n{iter_var}\n{iter_vect}\n{body}'


    
    
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
        space = '\t' * (tabs+2)
        attributes = space + 'Atributes' + '\n' + '\n'.join(self.visit(attr, tabs + 2) for attr in node.attributes)
        methods = space + 'Methods' + '\n' + f'\n{space} '.join(method for method in node.methods)
        return f'{ans}\n{attributes}\n{methods}'

    @visitor.when(cil.AllocateNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs)
        return f'{space}\\CallNode {node.dest} = ALOCATE {node.type.name}'
    
    @visitor.when(cil.OurFunctionNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__{node.__class__.__name__} {node.dest} = {node.name} {node.source}'
        return f'{ans}'
    
    @visitor.when(cil.ProgramNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs)
        dottypes = '\\__.TYPES\n' + f'{space} \n'.join(self.visit(t, tabs + 1) for t in node.dottypes)
        dotdata = '\\__.DATA\n' + f'{space} \n'.join(self.visit(t, tabs + 1) for t in node.dotdata)
        dotcode = '\\__.CODE\n' + f'{space} \n'.join(self.visit(t, tabs + 1) for t in node.dotcode)

        return f'{dottypes}\n{dotdata}\n{dotcode}'
    
    @visitor.when(cil.FunctionNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs)
        params = f'{space}\t \\__params\n' + '\n'.join(self.visit(x, tabs + 2) for x in node.params)
        localvars = f'{space}\t \\__local_vars\n' +  '\n'.join(self.visit(x, tabs + 2) for x in node.localvars)
        instructions = f'{space}\t \\__instructions\n' +  '\n'.join(self.visit(x, tabs + 2) for x in node.instructions)

        return f'{space} \\__FunctionNode function <{node.name}>\n{params}\n{localvars}\n{instructions}'
    
    @visitor.when(cil.StaticCallNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs)
        return f'{space}\\CallNode {node.dest} = call {node.function}'
    
    @visitor.when(cil.ReturnNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs)
        return f'{space}\\__ReturnNode return {node.value if node.value is not None else ""}'
    
    @visitor.when(cil.LocalNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs)
        return f'{space}\\__LocalNode {node.type} {node.name}'
    
    @visitor.when(cil.DataNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs)
        return f'{space}\\__DataNode {node.name} = {node.value}'
    
    @visitor.when(cil.ParamNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs)
        return f'{space}\\__ParamNode {node.name}'
    
    @visitor.when(cil.LabelNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs)
        return f'{space}\\__LabelNode {node.label}'
    
    @visitor.when(cil.GotoNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs)
        return f'{space}\\GotoNode {node.label}'
    
    @visitor.when(cil.GotoIfNode)
    def visit(self, node, tabs=0):
        space = '\t' * (tabs+1)
        ans = '\t' * tabs + f'\\__GotoIfNode:\n {space}\\__condition {node.condition} \n' + '\t' * (tabs+1) 
        return f'{ans}\\goto: {node.label}' + '\n' + '\t' * (tabs+1) + f'\\__else_goto: ' + f' {node.label_else}'
        
    @visitor.when(cil.AssignNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AsignNode: {node.dest} = {node.source}'
        return ans
    
    @visitor.when(cil.LoadNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__LoadNode: {node.dest} = LOAD {node.msg}'
        return ans
    
    @visitor.when(cil.OpenScope)
    def visit(self, node, tabs=0):
        return '\t' * tabs + '{\n'
    
    @visitor.when(cil.CloseScope)
    def visit(self, node, tabs=0):
        return '\t' * tabs + '}\n'
    
    @visitor.when(cil.Force)
    def visit(self, node, tabs=0):
        return f'{node.body}\n'
