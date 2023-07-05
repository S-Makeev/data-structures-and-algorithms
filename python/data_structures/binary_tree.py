class Node:
     def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


    def pre_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            value_list.append(input_node.value)
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def in_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            value_list.append(input_node.value)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def post_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)
            value_list.append(input_node.value)

        walk(self.root, values)
        return values

    def find_maximum_value(self):
        if self.root is None:
            raise Exception("Tree is empty.")

        max_value = None

        while self.root:
            if max_value is None or self.root.value > max_value:
                max_value = self.root.value

            if self.root.left and self.root.left.value > max_value:
                self.root = self.root.left
            elif self.root.right and self.root.right.value > max_value:
                self.root = self.root.right
            else:
                break

        return max_value
