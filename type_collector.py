import cmp.visitor as visitor
from nodes_types import hulk_types as hulk
from cmp.semantic import Context

class TypeCollector(object):
    def __init__(self, errors=[]):
        self.context = None
        self.errors = errors
    
    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(hulk.ProgramNode)
    def visit(self, node):
        self.context = Context()
        for statement in node.statements:
            self.visit(statement)
        return self.errors
            
    @visitor.when(hulk.TypeDeclarationNode)
    def visit(self, node):
        try:
            self.context.create_type(node.name)
        except:
            self.errors.append(f"La clase '{node.name}' ha sido definida más de una vez.")
        return self.errors
    