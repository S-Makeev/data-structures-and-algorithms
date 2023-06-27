class Node:
    def __init__(self,value, _next=None):
        self.value = value
        self._next = _next

class Stack:
  def __init__(self) -> None:
        self.top = None

  def push(self,value):
      node = Node(value)
      if self.top is None:
          self.top = node
      else:
          node.next = self.top
          self.top = node

  def pop(self):
      if self.top is None:
          raise Exception
      else:
          del_node = self.head
          del_node.next = None
          return del_node.value


# ALGORITHM pop()
#  INPUT <-- No input
#  OUTPUT <-- value of top Node in stack
#  EXCEPTION if stack is empty

#    Node temp <-- top
#    top <-- top.next
#    temp.next <-- null
#    return temp.value


#     ALOGORITHM push(value)
#  INPUT <-- value to add, wrapped in Node internally
#  OUTPUT <-- none
#    node = new Node(value)
#    node.next <-- Top
#    top <-- Node



