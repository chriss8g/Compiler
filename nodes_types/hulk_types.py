BOOL_TYPE = 'Boolean'
STRING_TYPE = 'String'
OBJECT_TYPE = 'Object'
NUMBER_TYPE = 'Number'
MY_TYPES = [BOOL_TYPE, STRING_TYPE, OBJECT_TYPE, NUMBER_TYPE]

class Node:
    pass

class ProgramNode(Node):
    def __init__(self, statements, main):
        self.statements = statements
        self.main = main


class StatementNode(Node):
    pass

class ProtocolNode(StatementNode):
    def __init__(self,name,extension,body):
        super().__init__()
        self.name = name
        self.extension = extension
        self.body = body

class MethodProtocolNode(Node):
    def __init__(self, name, args, type):
        super().__init__()
        self.name = name
        self.args = args
        self.type = type 

class FuncDeclarationNode(StatementNode):
    def __init__(self, name, body, params=None, type=None):
        super().__init__()
        self.name = name
        self.params = params if params else []# Array de tuplas (name,type) donde por defecto type es None
        self.body = body
        self.type = type
        
class TypeDeclarationNode(StatementNode):
    def __init__(self, name, body, params=None, base_type=OBJECT_TYPE, base_params=None):
        self.name = name
        self.body = body
        self.params = params if params else []
        self.base_type = base_type
        self.base_params = base_params if base_params else []
        
class TypeBodyDeclarationNode(Node):
    def __init__(self, attributes,methods):
        self.attributes = attributes
        self.methods = methods
        
class AttributeNode(Node):
    def __init__(self, idx, value, typex=None):
        self.id = idx
        self.value = value
        self.type = typex

class MethodNode(Node):
    def __init__(self, name, body, params=None, typex=None):
        self.name = name
        self.params = params if params else []
        self.body = body
        self.type = typex

class AssignNode(Node):
    def __init__(self, idx, expr,type=None):
        self.id = idx
        self.expr = expr
        self.type = type

class IterableNode(Node):
    def __init__(self, init, final):
        super().__init__()
        self.init = init
        self.final = final
        
        

# **************************************************
# ************     Dentro de MAIN     **************
# **************************************************

class ExpressionNode(Node):
    def __init__(self, type=None):
        self.type = type
        
class PrintNode(ExpressionNode):
    def __init__(self,expr):
        super().__init__(None)
        self.expr = expr

class BlockNode(ExpressionNode):
    def __init__(self, body, type=None):
        super().__init__(type)
        self.body = body  # es un array de expresiones

class LetNode(ExpressionNode):
    def __init__(self, args, body, type=None):
        super().__init__(type)
        self.args = args
        self.body = body

class WhileNode(ExpressionNode):
    def __init__(self, condition, body, type=None):
        super().__init__(type)
        self.condition = condition
        self.body = body

class ForNode(ExpressionNode):
    def __init__(self, idx, iterable, body, type=None):
        super().__init__(type)
        self.id = idx
        self.iterable = iterable
        self.body = body

class ForRangeNode(ExpressionNode):
    def __init__(self, idx, init, final, body, type=None):
        super().__init__(type)
        self.id = idx
        self.init = init
        self.final = final
        self.body = body
        
class IfNode(ExpressionNode):
    def __init__(self, condition, body, else_body, elif_conditions=None, elif_body=None, type=None):
        super().__init__(type)
        self.condition = condition if condition else []
        self.body = body
        self.else_body = else_body
        self.elif_conditions = elif_conditions if elif_conditions else []
        self.elif_body = elif_body if elif_body else []

class DestructNode(ExpressionNode):
    def __init__(self, idx, expr, type=None):
        super().__init__(type)
        self.id = idx
        self.expr = expr

class CallNode(ExpressionNode):
    def __init__(self, name, args=None, child=None, type=None):
        super().__init__(type)
        self.name = name
        self.args = args if args else [] # array de expresiones
        self.child = child

class VectorIndex(ExpressionNode):
    def __init__(self, name, index, type=None):
        super().__init__(type)
        self.name = name
        self.index = index

class IsNode(Node):
    def __init__(self, id, type):
        self.id = id
        self.type = type
        
class AsNode(Node):
    def __init__(self, id, type):
        self.id = id
        self.type = type
        

# **********************************************************
# *******************    Operaciones  **********************
# **********************************************************

class AtomicNode(ExpressionNode):
    def __init__(self, lex, type=None):
        super().__init__(type)
        self.lex = lex

class BinaryNode(ExpressionNode):
    def __init__(self, left, right, type=None):
        super().__init__(type)
        self.left = left
        self.right = right
        
class NumberOpNode(BinaryNode):
    def __init__(self, left, right):
        super().__init__(left, right, NUMBER_TYPE)

class StringOpNode(BinaryNode):
    def __init__(self, left, right):
        super().__init__(left, right, STRING_TYPE)

class BoolOpNode(BinaryNode):
    def __init__(self, left, right):
        super().__init__(left, right, BOOL_TYPE)
   
   
# *****************     Operaciones Aritmeticas     ***************** 

class AritmeticNode(NumberOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class PlusNode(AritmeticNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class MinusNode(AritmeticNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class StarNode(AritmeticNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class DivNode(AritmeticNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class PowNode(AritmeticNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class ModNode(AritmeticNode):
    def __init__(self, left, right):
        super().__init__(left, right)



# *****************     Operaciones Comparativas     ***************** 

class ComparativeNode(BoolOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class EQNode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class GTNode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class LTNode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class GENode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class LENode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class NENode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)


# *****************     Operaciones Logicas     ***************** 

class LogicalNode(BoolOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class AndNode(LogicalNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class OrNode(LogicalNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class NotNode(AtomicNode):
    def __init__(self, lex):
        super().__init__(lex, BOOL_TYPE)


# *****************     Operaciones con String     ***************** 


class ConcatNode(StringOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class ConcatSpaceNode(StringOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


# ***************      Expresiones atomicas      ******************

class SingleAritmeticOpNode(ExpressionNode):
    def __init__(self,expr):
        super().__init__(NUMBER_TYPE)
        self.expr = expr

class ObjectCreationNode(ExpressionNode):
    def __init__(self, type, args=None):
        super().__init__(type)
        self.args = args if args else []
        
class IdentifierNode(ExpressionNode):
    def __init__(self, name, child=None, type=None):
        super().__init__(type)
        self.name = name
        self.child = child
        
class SelfNode(ExpressionNode):
    def __init__(self, lex,type=None):
        super().__init__(type)
        self.lex = lex

class SinNode(SingleAritmeticOpNode):
    def __init__(self, expr):
        super().__init__(expr)
        

class CosNode(SingleAritmeticOpNode):
    def __init__(self, expr):
        super().__init__(expr)
        

class SqrtNode(SingleAritmeticOpNode):
    def __init__(self, expr):
        super().__init__(expr)
        

class ExpNode(SingleAritmeticOpNode):
    def __init__(self, expr):
        super().__init__(expr)
        

class LogNode(ExpressionNode):
    def __init__(self, base,arg):
        super().__init__(NUMBER_TYPE)
        self.base = base
        self.arg = arg

class RandNode(ExpressionNode):
    def __init__(self):
        super().__init__(NUMBER_TYPE)

class VectorNode(ExpressionNode):
    def __init__(self, items, type=None):
        super().__init__(type)
        self.items = items # array de los elementos del vector

class VectorImplicitNode(ExpressionNode):
    def __init__(self, expr, id, rangeLow, rangeUp, type=None):
        super().__init__(type)
        self.expr = expr
        self.id = id
        self.rangeLow = rangeLow
        self.rangeUp = rangeUp
        
#  Literales

class NumberNode(AtomicNode):
    def __init__(self, lex):
        super().__init__(lex, NUMBER_TYPE)

class StringNode(AtomicNode):
    def __init__(self, lex, type=STRING_TYPE):
        super().__init__(lex, type)

class BoolNode(AtomicNode):
    def __init__(self, lex, type=BOOL_TYPE):
        super().__init__(lex, type)

