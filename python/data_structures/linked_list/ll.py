# Create a Linked List class          V
# Within your Linked List class, include a head property.      V
# Upon instantiation, an empty Linked List should be created.     V
# The class should contain the following methods
# insert  V
# Arguments: value
# Returns: nothing
# Adds a new node with that value to the head of the list with an O(1) Time performance. V
# includes
# Arguments: value
# Returns: Boolean
# Indicates whether that value exists as a Node’s value somewhere within the list.
# to string
# Arguments: none
# Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"


class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next


class LinkedList:
    def __init__(self, head=None):
        self.head = head


    def traverse(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            print("List is not empty")
        while current is not None:
            current = current._next

    def insert(self, value):
         new_node = Node(value)
         new_node._next = self.head
         self.head = new_node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current._next
        return False

    def __str__(self):
        if self.head is None:
            return "NULL"
        else:
            current = self.head
            output = ""
            while current:
                output += f"{{ {current.value} }} -> "
                current = current._next
            output += "NULL"
            return output


if __name__ == '__main__':
  linkList = LinkedList()
  linkList.insert(20)
  linkList.insert(50)
  linkList.traverse()


