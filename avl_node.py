class AVL_Node:
    parent = None
    left = None
    right = None
    key = 0
    data = []

    def __init__(self, key, data):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.data = data

    def setRandomData(self):
        self.data = ['This', 'is', 'an', 'example', 'for', 'Data', 'Structure', 'II', 'Homework', '\'s', 'Python', 'AVL', 'Node']

    def setRandomKey(self):
        self.data = int(random() * 100)

    def killOwnParentsAndSiblings(self):
        self.parent = None
        self.left = self.right = None

    def insert(self, node, tree):
        if node.key == self.key:
            return
        if node.key < self.key:
            if self.left is None:
                self.left = node
                tree.count += 1
                return
            else:
                self.left.insert(node, tree)
                return
        if node.key > self.key:
            if self.right is None:
                self.right = node
                tree.count += 1
                return
            else:
                self.right.insert(node, tree)
                return