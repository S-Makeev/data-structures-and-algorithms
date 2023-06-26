from data_structures.stack import Stack
from data_structures.invalid_operation_error import InvalidOperationError


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        while not self.stack2.is_empty(): #Do While loop while stack2 is not empty
            self.stack1.push(self.stack2.pop()) #pop value from stack2 and push it into stack1
        self.stack1.push(value) # push passed value from enque into stack1

    def dequeue(self):
        while not self.stack1.is_empty(): #Do while loop while stack1 is not empty
            self.stack2.push(self.stack1.pop()) #pop value from stack1 and push into stack1
        if self.stack2.is_empty(): #Check if stack2 is empty
            raise IndexError("PseudoQueue is empty") #Raise exception
        return self.stack2.pop() # return the poppsed value from stack2


