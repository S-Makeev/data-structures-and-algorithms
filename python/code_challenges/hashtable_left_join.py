from data_structures.hashtable import Hashtable


def left_join(synonyms, antonyms):
    result = []
    for key in synonyms.keys():
        synonym_value = synonyms[key]
        antonym_value = antonyms.get(key, "NONE")
        result.append([key, synonym_value, antonym_value])
    return result




