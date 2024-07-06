INT_TYPE = 'int'
FLOAT_TYPE = 'float'
BOOL_TYPE = 'bool'
STRING_TYPE = 'string'
CONST_TYPE = 'const'
OBJECT_TYPE = 'object'
NUMBER_TYPE = [INT_TYPE, FLOAT_TYPE, CONST_TYPE]

class Node:
    pass

class ProgramNode(Node):
    def __init__(self, statements, main):
        self.statements = statements
        self.main = main


class StatementNode(Node):
    pass

class FuncDeclarationNode(StatementNode):
    def __init__(self, name, body, params=[], type=None):
        super().__init__()
        self.name = name
        self.params = params # Array de tuplas (name,type) donde por defecto type es None
        self.body = body
        self.type = type
        
class TypeDeclarationNode(StatementNode):
    def __init__(self, name, body, params=[], base_type=OBJECT_TYPE, base_params=[]):
        self.name = name
        self.body = body
        self.params = params
        self.base_type = base_type
        self.base_params = base_params
        
class TypeBodyDeclarationNode(Node):
    def __init__(self, attributes,methods):
        self.attributes = attributes
        self.methods = methods
        
class AttributeNode(Node):
    def __init__(self, name, value, type=None):
        self.name = name
        self.value = value
        self.type = type

class MethodNode(Node):
    def __init__(self, name, body, params=[], type=None):
        self.name = name
        self.params = params
        self.body = body
        self.type = type

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
        super().__init__(STRING_TYPE)
        self.expr = expr

class BlockNode(ExpressionNode):
    def __init__(self, body, type=None):
        super().__init__(type)
        self.body = body  # es un array de Sentences

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
    def __init__(self, condition, body, else_body, elif_conditions=[], elif_body=[], type=None):
        super().__init__(type)
        self.condition = condition
        self.body = body
        self.else_body = else_body
        self.elif_conditions = elif_conditions
        self.elif_body = elif_body

class DestructNode(ExpressionNode):
    def __init__(self, idx, expr, type=None):
        super().__init__(type)
        self.id = idx
        self.expr = expr

class CallNode(ExpressionNode):
    def __init__(self, idx, args, type=None):
        super().__init__(type)
        self.id = idx
        self.args = args # array de expresiones


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
    def __init__(self, left, right, type=NUMBER_TYPE):
        super().__init__(left, right, type)

class StringOpNode(BinaryNode):
    def __init__(self, left, right, type=STRING_TYPE):
        super().__init__(left, right, type)

class BoolOpNode(BinaryNode):
    def __init__(self, left, right, type=BOOL_TYPE):
        super().__init__(left, right, type)
   
   
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
        super().__init__(lex, type = BOOL_TYPE)


# *****************     Operaciones con String     ***************** 


class ConcatNode(StringOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class ConcatSpaceNode(StringOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


# ***************      Expresiones atomicas      ******************

class ObjectCreationNode(ExpressionNode):
    def __init__(self, type, args=[]):
        super().__init__(type)
        self.args = args
        
class IdentifierNode(ExpressionNode):
    def __init__(self, name, child=None, type=None):
        super().__init__(type)
        self.name = name
        self.child = child
        
class SelfNode(ExpressionNode):
    def __init__(self, lex,type=None):
        super().__init__(type)
        self.lex = lex

class SinNode(ExpressionNode):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr

class CosNode(ExpressionNode):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr

class SqrtNode(ExpressionNode):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr

class ExpNode(ExpressionNode):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr

class LogNode(ExpressionNode):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr

class RandNode(ExpressionNode):
    def __init__(self):
        super().__init__(NUMBER_TYPE)


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

