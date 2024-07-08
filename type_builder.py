import utils.visitor as visitor
from nodes_types import hulk_types as hulk
from utils.semantic import VariableInfo

class TypeBuilder:   
    def __init__(self, context, errors=[]):
        self.context = context
        self.current_type = None
        self.errors = errors
        self.var = []
    
    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(hulk.ProgramNode)
    def visit(self, node):
        for statement in node.statements:
            self.visit(statement)
        self.visit(node.main)
        return self.errors
    
    @visitor.when(hulk.FuncDeclarationNode)
    # falta verificar que el uso de los parametros sea consistente
    def visit(self, node):
        self.visit(node.body)
        if node.type:
            if node.type != node.body.type:
                5#self.errors.append(f"La función '{node.name}' debe retornar un '{node.type}'")
        else:
            node.type = node.body.type
        return self.errors
            
    @visitor.when(hulk.TypeDeclarationNode)
    # esto no hace nada
    def visit(self, node):
        self.visit(node.body)
        return self.errors
    
    @visitor.when(hulk.TypeBodyDeclarationNode)
    def visit(self,node):
        for attr in node.attributes:
            self.visit(attr)
        for meth in node.methods:
            self.vist(meth)
        return self.errors
            
    @visitor.when(hulk.AttributeNode)
    def visit (self, node):
        self.visit(node.value)
        if node.type:
            if node.type != node.value.type:
                5#self.errors.append(f"No se puede asignar un '{node.value.type}' a un '{node.type}'")
        else:
            node.type = node.value.type
        return self.errors
    
    @visitor.when(hulk.MethodNode)
    # falta verificar que el uso de los parametros sea consistente
    def visit(self, node):
        self.visit(node.body)
        if node.type:
            if node.type != node.body.type:
                5#self.errors.append(f"El método '{node.name}' debe retornar un '{node.type}'")
        else:
            node.type = node.body.type
        return self.errors
    
    @visitor.when(hulk.AssignNode)
    def visit(self, node):
        self.visit(node.expr)
        if node.id.type:
            if node.id.type != node.expr.type:
                5#self.errors.append(f"No se puede asignar un '{node.expr.type}' a un '{node.id.type}'")
        else:
            node.id.type = node.expr.type
            node.type = node.expr.type
            self.var.append(VariableInfo(node.id.name, node.id.type))
        return self.errors
    
    @visitor.when(hulk.BlockNode)
    def visit(self,node):
        for expr in node.body:
            self.visit(expr)
        node.type = node.body[-1].type
        return self.errors
    
    @visitor.when(hulk.LetNode)
    def visit(self,node):
        for arg in node.args:
            self.visit(arg)
        self.visit(node.body)
        node.type = node.body.type
        return self.errors
    
    @visitor.when(hulk.WhileNode)
    def visit(self,node):
        self.visit(node.condition)
        self.visit(node.body)
        node.type = node.body.type
        return self.errors
        
    @visitor.when(hulk.IfNode)
    # ancestro comun del no se que
    def visit(self,node):
        self.visit(node.condition)
        self.visit(node.body)
        node.type = node.body.type
        self.visit(node.else_body)
        for cond in node.elif_conditions:
            self.visit(cond)
        for body in node.elif_body:
            self.visit(body)
        return self.errors
    
    @visitor.when(hulk.DestructNode)
    def visit(self,node):
        self.visit(node.id)
        self.visit(node.expr)
        if node.id.type != node.expr.type:
            5#self.errors.append(f"No se puede asignar un '{node.expr.type}' a un '{node.id.type}'")
        else: 
            node.type = node.id.type
        return self.errors
    
    @visitor.when(hulk.CallNode)
    # to ta cabron
    def visit(self,node):
        return self.errors
    
    @visitor.when(hulk.PlusNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación + solo esta definida entre números")
        node.type = hulk.NUMBER_TYPE
        return self.errors
    
    @visitor.when(hulk.MinusNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación - solo esta definida entre números")
        node.type = hulk.NUMBER_TYPE
        return self.errors
    
    @visitor.when(hulk.StarNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación * solo esta definida entre números")
        node.type = hulk.NUMBER_TYPE
        return self.errors
    
    @visitor.when(hulk.DivNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación / solo esta definida entre números")
        node.type = hulk.FLOAT_TYPE
        return self.errors
    
    @visitor.when(hulk.PrintNode)
    def visit(self,node):
        self.visit(node.expr)
        node.type = node.expr.type if node.expr.type else hulk.INT_TYPE
        return self.errors
    
    @visitor.when(hulk.PowNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación ^ solo esta definida entre números")
        return self.errors
    
    @visitor.when(hulk.ModNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación % solo esta definida entre números")
        return self.errors
    
    @visitor.when(hulk.EQNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación == solo esta definida entre números")
        return self.errors
    
    @visitor.when(hulk.GTNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación > solo esta definida entre números")
        return self.errors
    
    @visitor.when(hulk.LTNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación < solo esta definida entre números")
        return self.errors
    
    @visitor.when(hulk.GENode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación >= solo esta definida entre números")
        return self.errors
    
    @visitor.when(hulk.LENode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación <= solo esta definida entre números")
        return self.errors
    
    @visitor.when(hulk.NENode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La operación != solo esta definida entre números")
        return self.errors
    
    @visitor.when(hulk.AndNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.BOOL_TYPE or node.right.type != hulk.BOOL_TYPE:
            5#self.errors.append(f"La operación & solo esta definida entre booleanos")
        return self.errors
    
    @visitor.when(hulk.OrNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.BOOL_TYPE or node.right.type != hulk.BOOL_TYPE:
            5#self.errors.append(f"La operación | solo esta definida entre booleanos")
        return self.errors
    
    @visitor.when(hulk.NotNode)
    def visit(self,node):
        if node.expr != hulk.BOOL_TYPE:
            5#self.errors.append(f"La operación ! solo esta definida para booleanos")
        return self.errors
    
    @visitor.when(hulk.ConcatNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.STRING_TYPE or node.right.type != hulk.STRING_TYPE:
            5#self.errors.append(f"La operación @ solo esta definida entre cadenas")
        return self.errors
    
    @visitor.when(hulk.ConcatSpaceNode)
    def visit(self,node):
        self.visit(node.left)
        self.visit(node.right)
        if node.left.type != hulk.STRING_TYPE or node.right.type != hulk.STRING_TYPE:
            5#self.errors.append(f"La operación @@ solo esta definida entre cadenas")
        return self.errors
    
    @visitor.when(hulk.IdentifierNode)
    def visit(self,node):
        for var in self.var:
            if var.name == node.name:
                node.type = var.type
                return self.errors
        5#self.errors.append(f"No existe la variable'{node.name}'")
        return self.errors
    
    # self
    
    @visitor.when(hulk.SinNode)
    def visit(self,node):
        self.visit(node.expr)
        if node.expr.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La función seno solo está definida en números")
        node.type = hulk.FLOAT_TYPE
        return self.errors
    
    @visitor.when(hulk.CosNode)
    def visit(self,node):
        self.visit(node.expr)
        if node.expr.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La función coseno solo está definida en números")
        node.type = hulk.FLOAT_TYPE
        
        return self.errors
    
    @visitor.when(hulk.SqrtNode)
    def visit(self,node):
        self.visit(node.expr)
        if node.expr.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La función raíz cuadrada solo está definida en números")
        node.type = hulk.FLOAT_TYPE
        return self.errors
    
    @visitor.when(hulk.ExpNode)
    def visit(self,node):
        self.visit(node.expr)
        if node.expr.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La función exponencial solo está definida en números")
        node.type = hulk.FLOAT_TYPE
        return self.errors
    
    @visitor.when(hulk.LogNode)
    def visit(self,node):
        self.visit(node.expr)
        if node.expr.type != hulk.NUMBER_TYPE:
            5#self.errors.append(f"La función logaritmo solo está definida en números")
        node.type = hulk.FLOAT_TYPE
        return self.errors
    
    