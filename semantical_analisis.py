class SemanticAnalyzer:
    def __init__(self, root):
        self.root = root

    def analyze(self):
        self.visit(self.root)

    def visit(self, node):
        method_name = f'visit_{node.__class__.__name__}'
        visitor = getattr(self, method_name, self.no_visit_method)
        return visitor(node)

    def no_visit_method(self, node):
        raise Exception(f"No visit_{node.__class__.__name__} method")

    # Ejemplo de método de visita para nodos de tipo Number
    def visit_Number(self, node):
        return "number"

    # Ejemplo de método de visita para nodos de tipo BinaryOperation
    def visit_BinaryOperation(self, node):
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)

        if left_type!= "number" or right_type!= "number":
            print("Error: Operación entre tipos no numéricos")
            return False

        # Aquí puedes agregar más lógica para manejar diferentes tipos de operaciones
        return True