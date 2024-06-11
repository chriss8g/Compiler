class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

class Number(Node):
    def __init__(self, value):
        self.value = value

class BinaryOperation(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

def print_node_info(node):
    if isinstance(node, Number):
        print(f"Type: Number, Value: {node.value}")
    elif isinstance(node, BinaryOperation):
        print(f"Type: BinaryOperation, Left: {print_node_info(node.left)}, Operator: {node.op}, Right: {print_node_info(node.right)}")
    else:
        print(f"Unknown type: {type(node).__name__}")

def parse_ast_from_tuple(ast_tuple):
    if isinstance(ast_tuple, tuple):
        operator = ast_tuple[0]
        operands = ast_tuple[1:]
        # Asignar el tipo de nodo a BinaryOperation
        node = BinaryOperation(left=None, op=operator, right=None)
        for i, operand in enumerate(operands):
            if isinstance(operand, tuple):
                # Recursivamente parsear el subnodo
                child_node = parse_ast_from_tuple(operand)
                if i == 0:
                    node.left = child_node
                elif i == len(operands) - 1:
                    node.right = child_node
            else:
                # Asignar el tipo de nodo a Number
                node = Number(value=operand)
        return node
    else:
        return Number(value=ast_tuple)