INT_TYPE = 'int'
FLOAT_TYPE = 'float'
BOOL_TYPE = 'bool'
STRING_TYPE = 'string'
CONST_TYPE = 'const'
NUMBER_TYPE = [INT_TYPE, FLOAT_TYPE, CONST_TYPE]

# Nivel 0

class Node:
    pass

# Nivel 1

class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements

class StatementNode(Node):
    pass

class ExpressionNode(Node):
    def __init__(self):
        self.type = None

# Nivel 2

class VarDeclarationNode(StatementNode, ExpressionNode):
    def __init__(self, args, body):
        super().__init__()
        self.args = args
        self.body = body

class FuncDeclarationNode(StatementNode, ExpressionNode):
    def __init__(self, idx, params, body, type):
        super().__init__()
        self.id = idx
        self.params = params
        self.body = body
        self.type = type

class PrintNode(ExpressionNode):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr

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
        super().__init__()

class ForNode(StatementNode, ExpressionNode):
    def __init__(self, idx, iterable, expr):
        super().__init__()
        self.id = idx
        self.iterable = iterable
        self.expr = expr

class AsignNode(StatementNode, ExpressionNode):
    def __init__(self, idx, expr):
        super().__init__()
        self.id = idx
        self.expr = expr

class DestructNode(StatementNode, ExpressionNode):
    def __init__(self, idx, expr):
        self.id = idx
        self.expr = expr

class WhileNode(StatementNode, ExpressionNode):
    def __init__(self, condition, expr):
        super().__init__()
        self.condition = condition
        self.expr = expr

class IfNode(StatementNode, ExpressionNode):
    def __init__(self, condition, expr, else_expr, elif_conditions, elif_expr):
        super().__init__()
        self.condition = condition
        self.expr = expr
        self.else_expr = else_expr
        self.elif_conditions = elif_conditions
        self.elif_expr = elif_expr

class IterableNode(ExpressionNode):
    def __init__(self, init, final):
        super().__init__()
        self.init = init
        self.final = final

class BlockNode(ExpressionNode):
    def __init__(self, body):
        super().__init__()
        self.body = body

class AtomicNode(ExpressionNode):
    def __init__(self, lex):
        super().__init__()
        self.lex = lex

class BinaryNode(ExpressionNode):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

class CallNode(ExpressionNode):
    def __init__(self, idx, args):
        super().__init__()
        self.id = idx
        self.args = args

# Nivel 3

class ConstantNumNode(AtomicNode):
    def __init__(self, lex):
        super().__init__(lex)

class BoolNode(AtomicNode):
    def __init__(self, lex):
        super().__init__(lex)

class StringNode(AtomicNode):
    def __init__(self, lex):
        super().__init__(lex)

class VariableNode(AtomicNode):
    def __init__(self, name, var_type=None):
        super().__init__(name)  # Asumiendo que el nombre es el valor léxico de la variable
        self.name = name
        self.var_type = var_type  # Esto puede ser None o un tipo específico como 'int', 'float', etc.

class ComparativeNode(BinaryNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class TypedVariable(BinaryNode):
    pass

class LogicNode(BinaryNode, AtomicNode):
    def __init__(self, left, right):
        BinaryNode.__init__(self, left, right)
        AtomicNode.__init__(self, None)

class AritmeticNode(BinaryNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class StringOpNode(BinaryNode):
    def __init__(self, left, right):
        super().__init__(left, right)

# Nivel 4

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

class AndNode(LogicNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class OrNode(LogicNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class ConcatNode(StringOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class NotNode(LogicNode):
    def __init__(self, expr):
        super().__init__(None, expr)
        self.expr = expr

class EqualNode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class NotEqualNode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class GreaterNode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class LessNode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class GreaterEqualNode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class LessEqualNode(ComparativeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class ConcatNode(StringOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class ForRangeNode(StatementNode):
    def __init__(self, idx, init, final, body):
        super().__init__()
        self.id = idx
        self.init = init
        self.final = final
        self.body = body

class ConcatSpaceNode(BinaryNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class SelfNode(AtomicNode):
    def __init__(self, lex):
        super().__init__(lex)

class TypeNode(Node):
    def __init__(self, name, body, base_type=None, params=None):
        self.name = name
        self.body = body
        self.base_type = None
        if base_type is not None:
            self.base_type = base_type
        self.params = params if params is not None else []  # Lista de diccionarios con 'name' y 'type' para cada parámetro

class TypeBodyNode(Node):
    def __init__(self, attributes,methods):
        self.attributes = attributes
        self.methods = methods

class AttributeNode(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class MethodNode(Node):
    def __init__(self, name, parameters, body, type=None):
        self.name = name
        self.parameters = parameters
        self.body = body
        self.type = type

class ObjectCreationNode(ExpressionNode):
    def __init__(self, type_name, arguments):
        super().__init__()
        self.type_name = type_name
        self.arguments = arguments

class IdentifierNode(ExpressionNode):
    def __init__(self, name, child=None):
        super().__init__()
        self.name = name
        self.child = child
        
class MethodCallNode(ExpressionNode):
    def __init__(self, name, arguments):
        super().__init__()
        self.name = name
        self.arguments = arguments
