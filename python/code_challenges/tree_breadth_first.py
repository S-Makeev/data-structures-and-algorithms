from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue

def breadth_first(tree):
    if tree.root is None:
        return []

    result = []
    breadth = Queue()
    breadth.enqueue(tree.root)

    while not breadth.is_empty():
        front = breadth.dequeue()
        result.append(front.value)

        if front.left is not None:
            breadth.enqueue(front.left)

        if front.right is not None:
            breadth.enqueue(front.right)

    return result





















# ALGORITHM breadthFirst(root)

#   Queue breadth <-- new Queue()
#   breadth.enqueue(root)

#   while ! breadth.is_empty()
#     node front = breadth.dequeue()
#     OUTPUT <-- front.value

#     if front.left is not NULL
#       breadth.enqueue(front.left)

#     if front.right is not NULL
#       breadth.enqueue(front.right)
