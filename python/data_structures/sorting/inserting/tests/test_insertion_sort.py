import pytest
from selection_sort import Insert, InsertionSort

def test_Insert():
    sorted_array = [4, 8, 23, 42]

    Insert(sorted_array, 16)
    assert sorted_array == [4, 8, 16, 23, 42]

    Insert(sorted_array, 10)
    assert sorted_array == [4, 8, 10, 16, 23, 42]

    Insert(sorted_array, 30)
    assert sorted_array == [4, 8, 10, 16, 23, 30, 42]

    Insert(sorted_array, 5)
    assert sorted_array == [4, 5, 8, 10, 16, 23, 30, 42]

    Insert(sorted_array, 1)
    assert sorted_array == [1, 4, 5, 8, 10, 16, 23, 30, 42]


def test_InsertionSort():
    input_array = [8, 4, 23, 42, 16, 15]
    sorted_array = InsertionSort(input_array)

    assert sorted_array == [4, 8, 15, 16, 23, 42]

    input_array = [3, 1, 5, 2, 4]
    sorted_array = InsertionSort(input_array)

    assert sorted_array == [1, 2, 3, 4, 5]


def test_function_existence():
    assert callable(Insert)
    assert callable(InsertionSort)


# Run the tests
if __name__ == "__main__":
    pytest.main()
