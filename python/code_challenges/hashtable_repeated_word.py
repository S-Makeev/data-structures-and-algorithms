from data_structures.hashtable import Hashtable
import re
#TODO Write a function called repeated word that finds the first word to occur more than once in a string
# Arguments: string
# Return: string

def first_repeated_word(_str):

    stripped_str = re.sub(r'[^\w\s]', '', _str)
    word_str = Hashtable()

    words = re.findall(r'\b\w+\b', stripped_str.lower())

    for word in words:
        if word_str.has(word):
            return word
        else:
            word_str.set(word, True)
    return None
