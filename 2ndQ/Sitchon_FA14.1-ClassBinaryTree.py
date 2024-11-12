class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

# root layer
root = Node(1)

# first child layer
root.left = Node(2)
root.right = Node(3)

# second child layer
root.left.left = Node(4)
root.left.right = Node(5)

# Tree structure
#       1
#      / \
#     2   3
#    / \
#   4   5