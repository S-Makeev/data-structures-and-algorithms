from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree import Node

class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        self.root = root


    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    break
            elif value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    break
            else:
                break

        # There's a root => check value, create a new_node
    def contains(self, value):
       current = self.root
       while current:
           if current.value == value:
               return True
           elif value < current.value:
               current = current.left
           else:
               current = current.right
       return False
