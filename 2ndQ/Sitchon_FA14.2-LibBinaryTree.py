from binarytree import Node

# root layer
root = Node(1)

# first child layer
root.left = Node(2)
l = root.left
root.right = Node(3)
r = root.right

# second child layer
l.left = Node(4)
l.right = Node(5)

print(root)