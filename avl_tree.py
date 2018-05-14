import AVL_Node from avl_node

class AVL_Tree:
    height = 0
    count = 0
    root = None

    def __init__(self):
        self.height = 0
        self.count = 0
        self.root = None
    
    def add(self, node):
        # Primeiro caso: verifica se a árvore é vazia
        if (self.root is None):
            print("OK!")
            self.root = node
            return
        else:
            # Próximas inserções
            root.insert(node, self)

        # Rebalanceia a árvore (rotações)
            
        # Atualiza-se os índices (count, height)

    def remove(self, key):
        # Verifica-se a árvore está vazia
        if self.root is None:
            # Caso esteja, retornar
            return
        else:
            # Caso contrário, chamar a função de remoção do nó raíz
            self.root.remove(key, self)

        # Rebalanceia a árvore (rotações)

        # Atualiza-se os índices (count, height)

    def printTree(self):
        print("{ " + str(self.key) + " : " + str(self.data) + " }")

    def autobalance(self):
        pass

    def getLowestElement(self):
        pass
    def getHighestElement(self):
        pass

    def getTreeMaximiumHeight(self):
        pass

    def print_preordem(self):
        pass
    def print_inordem(self):
        pass
    def print_posordem(self):
        pass
