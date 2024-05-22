class ASTNode:
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        self.children = children if children is not None else []
        self.leaf = leaf
        self.data_type = None  # Añadido para el chequeo semántico
        self.tac_var = None  # Variable temporal para TAC

    def __repr__(self):
        return f"ASTNode(type={self.type}, leaf={self.leaf}, children={self.children})"

    def imprimir(self, nivel=0):
        print(' ' + str(nivel) + ' ' + ' ' + str(self.leaf))
        for child in self.children:
            child.imprimir(nivel=nivel+1)