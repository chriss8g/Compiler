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
        self.args = args
        self.body = body

class FuncDeclarationNode(StatementNode, ExpressionNode):
    def __init__(self, idx, params, body, type=None):
        self.id = idx
        self.params = params
        self.body = body
        self.type = type

class PrintNode(ExpressionNode):
    def __init__(self, expr):
        self.expr = expr

class SinNode(ExpressionNode):
    def __init__(self, expr):
        self.expr = expr

class CosNode(ExpressionNode):
    def __init__(self, expr):
        self.expr = expr

class SqrtNode(ExpressionNode):
    def __init__(self, expr):
        self.expr = expr

class ExpNode(ExpressionNode):
    def __init__(self, expr):
        self.expr = expr

class LogNode(ExpressionNode):
    def __init__(self, expr):
        self.expr = expr

class RandNode(ExpressionNode):
    pass

class ForNode(StatementNode, ExpressionNode):
    def __init__(self, idx, iterable, expr):
        self.id = idx
        self.iterable = iterable
        self.expr = expr

class AsignNode(StatementNode, ExpressionNode):
    def __init__(self, idx, expr):
        self.id = idx
        self.expr = expr

class DestructNode(StatementNode, ExpressionNode):
    def __init__(self, idx, expr):
        self.id = idx
        self.expr = expr

class WhileNode(StatementNode, ExpressionNode):
    def __init__(self, condition, expr):
        self.condition = condition
        self.expr = expr

class IfNode(StatementNode, ExpressionNode):
    def __init__(self, condition, expr, else_expr, elif_conditions, elif_expr):
        self.condition = condition
        self.expr = expr
        self.else_expr = else_expr
        self.elif_conditions = elif_conditions
        self.elif_expr = elif_expr

class IterableNode(ExpressionNode):
    def __init__(self, init, final):
        self.init = init
        self.final = final

class BlockNode(StatementNode):
    def __init__(self, body):
        self.body = body

class AtomicNode(ExpressionNode):
    def __init__(self, lex):
        self.lex = lex

class BinaryNode(ExpressionNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class CallNode(ExpressionNode):
    def __init__(self, idx, args):
        self.id = idx
        self.args = args

# Nivel 3

class ConstantNumNode(AtomicNode):
    pass

class BoolNode(AtomicNode):
    pass

class StringNode(AtomicNode):
    pass

class VariableNode(AtomicNode):
    def __init__(self, name, var_type=None):
        super().__init__(name)  # Asumiendo que el nombre es el valor léxico de la variable
        self.name = name
        self.var_type = var_type  # Esto puede ser None o un tipo específico como 'int', 'float', etc.

class ComparativeNode(BinaryNode):
    pass

class TypedVariable(BinaryNode):
    pass

class LogicNode(BinaryNode, AtomicNode):
    pass

class AritmeticNode(BinaryNode):
    pass

class StringOpNode(BinaryNode):
    pass

# Nivel 4

class PlusNode(AritmeticNode):
    pass

class MinusNode(AritmeticNode):
    pass

class StarNode(AritmeticNode):
    pass

class DivNode(AritmeticNode):
    pass

class PowNode(AritmeticNode):
    pass

class ModNode(AritmeticNode):
    pass

class EQNode(ComparativeNode):
    pass

class GTNode(ComparativeNode):
    pass

class LTNode(ComparativeNode):
    pass

class GENode(ComparativeNode):
    pass

class LENode(ComparativeNode):
    pass

class NENode(ComparativeNode):
    pass

class AndNode(LogicNode):
    pass

class OrNode(LogicNode):
    pass

class ConcatNode(StringOpNode):
    pass

class NotNode(LogicNode):
    def __init__(self, expr):
        self.expr = expr

class EqualNode(ComparativeNode):
    pass

class NotEqualNode(ComparativeNode):
    pass

class GreaterNode(ComparativeNode):
    pass

class LessNode(ComparativeNode):
    pass

class GreaterEqualNode(ComparativeNode):
    pass

class LessEqualNode(ComparativeNode):
    pass

class ConcatNode(StringOpNode):
    pass

class ForRangeNode(StatementNode):
    def __init__(self, idx, init, final, body):
        self.id = idx
        self.init = init
        self.final = final
        self.body = body

class ConcatSpaceNode(BinaryNode):
    def __init__(self, left, right):
        super().__init__(left, right)

class SelfNode(AtomicNode):
    pass

class TypeNode(Node):
    def __init__(self, name, body, base_type=None, params=None):
        self.name = name
        self.body = body
        self.base_type = base_type[0]
        self.params = params if params is not None else []  # Lista de diccionarios con 'name' y 'type' para cada parámetro

class TypeBodyNode(Node):
    def __init__(self, attributes_and_methods):
        self.attributes = attributes_and_methods[0]
        self.methods = attributes_and_methods[1]

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
        self.type_name = type_name
        self.arguments = arguments

class MethodCallNode(ExpressionNode):
    def __init__(self, object_name, method_name, arguments):
        self.object_name = object_name
        self.method_name = method_name
        self.arguments = arguments
