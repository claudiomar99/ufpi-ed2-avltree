class AVL_NODE():
    # Construtor

    def __init__(self, key, data):
        self.key = key  # Chave do Nó
        self.data = []  # Lista de Dados

        self.left = None  # Referência ao filho à esquerda
        self.right = None  # Referência ao filho à direita
        self.parent = None  # Referência ao pai

        self.balancingFactor = 0  # Fator de Balanceamento

    def __str__(self):
        # Define a forma como será representado o objeto na função print()
        return "{ " + str(self.key) + " : " + str(self.data) + " }"

    # Funções de Rotação

    def rotateLeft(self):
        # O filho a direita (denominado de X, temporariamente) deste nó passa a ser a raíz.
        # O filho a esquerda de X passa a ser o filho a direita da raíz original
        # A raíz passa a ser o filho a esquerda de X
        pass

    def rotateRight(self):
        pass

    def rotateDoubleLeft(self):
        pass

    def rotateDoubleRight(self):
        pass

    # Funções de Cálculo

    def recompute_heights(self, start_from_node):
        changed = True
        node = start_from_node
        while node and changed:
            old_height = node.height
            node.height = (node.max_children_height() + 1 if (node.rightChild or node.leftChild) else 0)
            changed = node.height != old_height
            node = node.parent

    def calculateBalancingFactor(self):
        pass

    # Funções de Impressão

    def printNodeKeyAndBalancingFactor(self):
        print("{‘chave do nó’: [FB do nó]}")
        pass

    def printNodeContent(self):
        print("{‘Nó XXXX’: [chave do filho a esquerda, chave do filho a direita], [dados]}.")
        pass

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print(self)
        if self.right:
            self.right.printInOrder()

    # Função para Encontrar

    def find(self, key):
        return self.findInTree(self.rootReference, key)
        pass

    def findInTree(self, starting_node, key):
        if starting_node is None:
            return None
        if key < starting_node.key:
            return self.findInTree(starting_node.left, key)
        elif key > starting_node.key:
            return self.findInTree(starting_node.right, key)
        else:
            return starting_node

    def getHighestKey(self):
        if self.right:
            return self.right.getHighestKey()
        else:
            return self

    def getLowestKey(self):
        if self.left:
            return self.left.getLowestKey()
        else:
            return self

    # Funções de Adição e Remoção de Nós

    def insert(self, node):
        if self is None:
            self = node
        if node.key < self.key:
            # Inserção a esquerda
            if self.left:
                self.left.insert(node)
            else:
                node.parent = self
                self.left = node
        elif node.key > self.key:
            if self.right:
                self.right.insert(node)
            else:
                node.parent = self
                self.right = node
        return self.parent

    def remove(self, key):
        pass
