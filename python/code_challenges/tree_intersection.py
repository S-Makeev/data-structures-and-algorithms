from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable

def tree_intersection(tree1, tree2):
    values_set1 = set(tree1.in_order())
    values_set2 = set(tree2.in_order())

    hashmap = Hashtable()
    for value in values_set1:
        hashmap.set(value, True)

    intersection_list = []
    for value in values_set2:
        if hashmap.has(value):
            intersection_list.append(value)

    return intersection_list



