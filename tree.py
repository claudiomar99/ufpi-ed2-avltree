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
        self.rebalanceTree()

    def rebalanceTree(self, node):
        pass

    def updateBalance(self, node):
        pass

    def updateHeight(self, node):
        if not node:
            return -1
        else:
            return 1 + max(self.updateHeight(node.left), self.updateHeight(node.right))