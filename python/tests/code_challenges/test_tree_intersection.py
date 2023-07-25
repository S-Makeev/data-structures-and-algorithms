import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


#@pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)


def test_uneven_negative_tree_intersection():

    tree_a = BinaryTree()
    values = [100, 400, 250, 800, 150, 200, -300]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [500, 250, 150, 100, -300]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [-300, 100, 150, 250]

    assert sorted(actual) == sorted(expected)

def test_duplicate_tree_intersection():

    tree_a = BinaryTree()
    values = [100, 400,  250, -140, 250, 800, 150, 200, 250 ]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [500, 500, 250, 150, 100, 150, -280, 800,]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [100, 150, 250, 800]

    assert sorted(actual) == sorted(expected)
