from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    This object should be aware of a default empty value assigned to top when the stack is created.
    """
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        if self.top is None:
           self.top = node
        else:
            node.next = self.top
            self.top = node

        """
        ALOGORITHM push(value)
         INPUT <-- value to add, wrapped in Node internally
         OUTPUT <-- none
           node = new Node(value)
           node.next <-- Top
           top <-- Node
        """
    # push
    # Arguments: value
    # adds a new node with that value to the top of the stack with an O(1) Time performance.


    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        node_temp = self.top
        self.top = self.top.next
        node_temp.next = None
        return node_temp.value

#     ALGORITHM pop()
#  INPUT <-- No input
#  OUTPUT <-- value of top Node in stack
#  EXCEPTION if stack is empty

#    Node temp <-- top
#    top <-- top.next
#    temp.next <-- null
#    return temp.value
    # pop
    # Arguments: none
    # Returns: the value from node from the top of the stack
    # Removes the node from the top of the stack
    # Should raise exception when called on empty stack


    def peek(self):
      if self.top is None:
          raise InvalidOperationError("Method not allowed on empty collection")
      return self.top.value

    # peek
    # Arguments: none
    # Returns: Value of the node located at the top of the stack
    # Should raise exception when called on empty stack


# ALGORITHM peek()
#  INPUT <-- none
#  OUTPUT <-- value of top Node in stack
#  EXCEPTION if stack is empty

#    return top.value
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False


    # is empty
    # Arguments: none
    # Returns: Boolean indicating whether or not the stack is empty.
