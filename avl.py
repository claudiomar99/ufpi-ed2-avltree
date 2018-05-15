# import random, math

debugEnable = True

def debug(string):
    if debugEnable is True:
        print(string)


class Node():
    # Construtor do Nó
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return "{ '" + str(self.key) + "' : " + str(self.data) + " }"


class AVLTree():
    # Construtor da Árvore
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0;

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        tree = self.node

        newnode = Node(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Nó (" + str(key) + ") inserido")

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        else:
            debug("Nó (" + str(key) + ") já existe na árvore.")

        self.rebalance()

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        debug('Rotacionando ' + str(self.node.key) + ' para a direita')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        debug('Rotacionando ' + str(self.node.key) + ' para a esquerda')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, key):
        if self.node != None:
            if self.node.key == key:
                debug("Removendo: " + str(key))
                # Se o nó for uma folha, simpelsmente remover.
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None
                # Se o nó tiver não tiver um filho a esquerda, mas tiver o da direita, tornar o filho a direita a raíz
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                # Se o nó tiver não tiver um filho a direita, mas tiver o da esquerda, tornar o filho a esquerda a raíz
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # Caso não seja nenhum dos casos acima, devolver o nó sucessor.
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # Verifica se o nó para substituir não é vazio
                        debug("Substituindo " + str(key) + " por " + str(replacement.key))
                        self.node.key = replacement.key
                        self.node.right.delete(replacement.key)

                # Chama a função para rebalancear árvore
                self.rebalance()
                return

            # Se não for o nó desejado, procurar nas suas sub-árvores
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return

    # Retorna o predecessor lógico
    def logical_predecessor(self, node):
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    # Retorna o sucessor lógico
    def logical_successor(self, node):
        node = node.right.node
        if node != None:
            while node.left != None:
                debug("Procurando sucessor. Atual: " + str(node.key))
                if node.left.node == None:
                    debug("Fim da pesquisa de nó sucessor. Encontrado: " + str(node.key))
                    return node
                else:
                    node = node.left.node
        return node

    # Verifica se a árvore está balanceada
    def check_balanced(self):
        if self == None or self.node == None:
            return True
        self.update_heights()
        self.update_balances()
        ## ABS: retorna o valor absoluto. Verifica se a função está balanceada, retornando "false" caso não.
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    # Preenche um vetor com as chaves em-ordem.
    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    # DEBUG: Mostra a árvore via prompt de comando.
    def display(self, level=0, pref=''):
        self.update_heights()
        self.update_balances()
        if (self.node != None):
            print ('.' * level * 3, pref, self.node.key, "(Altura: " + str(self.height) + "| FB: " + str(
                self.balance) + ")", '[FOLHA]' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, 'LN')
            if self.node.left != None:
                self.node.right.display(level + 1, 'RN')


# Usage example
if __name__ == "__main__":
    a = AVLTree()
    print("----- Inserting -------")
    # inlist = [5, 2, 12, -4, 3, 21, 19, 25]
    inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
    for i in inlist:
        a.insert(i)

    a.display()

    print("----- Deleting -------")
    a.delete(3)
    a.delete(4)
    # a.delete(5)
    a.display()

    print()
    print("Input            :", inlist)
    print("deleting ...       ", 3)
    print("deleting ...       ", 4)
    print("Inorder traversal:", a.inorder_traverse())
