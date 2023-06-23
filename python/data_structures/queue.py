from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Put docstring here
    """
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
       new_node = Node(value)
       if self.front is None:
          self.front = new_node
          self.rear = new_node
       else:
           self.rear.next = new_node
           self.rear = new_node


    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        if self.front is None:
            self.back = None
        return temp.value

    def peek(self):
        front_node = self.front
        if self.front is None:
            raise  InvalidOperationError("Method not allowed on empty collection")
        else:
            return front_node.value


    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
#     ALGORITHM isEmpty()
#  INPUT <-- none
#  OUTPUT <-- boolean

# return front = NULL

#         ALGORITHM peek()
# / INPUT <-- none
# / OUTPUT <-- value of the front Node in Queue
# / EXCEPTION if Queue is empty

#    return front.value
