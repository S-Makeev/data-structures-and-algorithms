from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue

def fizz_buzz_tree(tree):
    if not tree:
        return None

    new_tree = KaryTree(Node(str(tree.root.value)))
    queue = Queue()
    queue.enqueue((tree.root, new_tree.root))

    while not queue.is_empty():
        original_node, new_node = queue.dequeue()

        if original_node.value % 3 == 0 and original_node.value % 5 == 0:
            new_node.value = "FizzBuzz"
        elif original_node.value % 3 == 0:
            new_node.value = "Fizz"
        elif original_node.value % 5 == 0:
            new_node.value = "Buzz"
        else:
            new_node.value = str(original_node.value)

        for child in original_node.children:
            new_child = Node(child.value)
            new_node.children.append(new_child)
            queue.enqueue((child, new_child))

    return new_tree

def get_node_values_as_list(tree):
    values = []
    queue = Queue()
    queue.enqueue(tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        values.append(str(node.value))

        for child in node.children:
            queue.enqueue(child)

    return values
