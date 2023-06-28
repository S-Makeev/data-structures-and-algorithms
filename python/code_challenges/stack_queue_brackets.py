from data_structures.queue import Queue
from data_structures.stack import Stack

def multi_bracket_validation(_str):
    coolStack = Stack()

    left_bracket = ['(', '{', '[']
    right_bracket = [')', '}', ']']


    for char in _str:
        if char in left_bracket:
            coolStack.push(char)
        elif char in right_bracket:
            if coolStack.is_empty():
                return False
            top = coolStack.pop()
            if left_bracket.index(top) != right_bracket.index(char):
                return False

    return coolStack.is_empty()




