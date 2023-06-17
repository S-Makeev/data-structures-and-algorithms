import pytest
from ll import Node, LinkedList

#     Write tests to prove the following functionality:

# Can successfully instantiate an empty linked list V
# Can properly insert into the linked list V
# The head property will properly point to the first node in the linked list V
# Can properly insert multiple nodes into the linked list   V
# Will return true when finding a value within the linked list that exists V
# Will return false when searching for a value in the linked list that does not exist V
# Can properly return a collection of all the values that exist in the linked list V

def test_to_string():
    linked_list = LinkedList()
    linked_list.insert("1")
    linked_list.insert("2")
    linked_list.insert("3")
    assert str(linked_list) == "{ 3 } -> { 2 } -> { 1 } -> NULL"

def test_value_dont_exist():
    ll = LinkedList()
    ll.insert(15)
    ll.insert(130)
    ll.insert(924)
    assert ll.includes(233) is False


def test_value_exist():
    ll = LinkedList()
    ll.insert(15)
    ll.insert(130)
    ll.insert(924)
    assert ll.includes(130)


def test_insert_multiple():
    ll = LinkedList()
    ll.insert(24)
    ll.insert(12)
    assert ll.head.value == 12
    assert ll.head._next.value == 24


def test_empty():
    actual = Node([])
    expected = []
    assert actual.value == expected


def test_insert_list():
    ll = LinkedList()
    ll.insert(12)
    assert ll.head.value == 12


def test_head():
    ll = LinkedList()
    assert ll.head is None

