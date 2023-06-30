from data_structures.queue import Queue
from data_structures.stack import Stack

def multi_bracket_validation(_str):
    coolStack = Stack()

    left_bracket = ['(', '{', '[']
    right_bracket = [')', '}', ']']


    for bracket in _str:
        if bracket in left_bracket:
            coolStack.push(bracket)
        elif bracket in right_bracket:
            if coolStack.is_empty():
                return False
            top = coolStack.pop()
            if left_bracket.index(top) != right_bracket.index(bracket):
                return False

    return coolStack.is_empty()




