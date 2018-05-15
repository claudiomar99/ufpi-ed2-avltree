import avl
import tree

node = avl.AVL_NODE(10,[])

print(node)

node.insert(avl.AVL_NODE(15,[]))
node.insert(avl.AVL_NODE(5,[]))
node.insert(avl.AVL_NODE(1,[]))
node.insert(avl.AVL_NODE(17,[]))
node.insert(avl.AVL_NODE(20,[]))
node.insert(avl.AVL_NODE(12,[]))

node.printInOrder()