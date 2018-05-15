import avl

class AVL_TREE:
    def __init__(self):
        self.root = None

    def insert(self,node):
        # Atualiza a árvore
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

        # Balanceia a árvore