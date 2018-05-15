class AVL_NODE():
    key = 0             # Chave do Nó
    data = []           # Lista de Dados
    balancingFactor = 0
    left = None         # Referência ao filho à esquerda
    right = None        # Referência ao filho à direita
    parent = None       # Referência ao pai

    # Construtor

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = self.right = self.parent = None

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

    def calculateHeight(self):
        pass
    def calculateBalancingFactor(self):
        pass

    # Funções de Impressão

    def printNodeKeyAndBalancingFactor(self):
        print("{‘chave do nó’: [FB do nó]}")
        pass

    def printNodeContent(self):
        print("{‘Nó XXXX’: [chave do filho a esquerda, chave do filho a direita], [dados]}.")
        pass

    # Funções de Adição e Remoção de Nós

    def add(self, node):
        pass

    def remove(self, key):
        pass
