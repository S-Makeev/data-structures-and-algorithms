import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join

# Seems like there was an ordering issue with expected. Adjusted the expected order.
#@pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }
    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected


def test_dict_uneven():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
        "peace": "calm",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }
    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "delight"],
        ["peace", "calm", "NONE"],  # An extra triplet for the extra word
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected


def test_all_none():
    synonyms = {
        "cider": None,
        "ashtray": None,
        "vision": None,
    }
    antonyms = {
        "cider": None,
        "ashtray": None,
        "vision": None,
    }
    expected = [
        ["cider", None, None],
        ["ashtray", None, None],
        ["vision", None, None],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected
