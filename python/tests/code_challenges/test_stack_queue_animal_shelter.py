import pytest
from code_challenges.stack_queue_animal_shelter import AnimalShelter, Dog, Cat


#@pytest.mark.skip("TODO")
def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_dog_preferred_but_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


#@pytest.mark.skip("TODO")
def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("lizard")
    expected = None
    assert expected == actual

#Test if the order remains the same after DQ and EQ
def test_enqueue_dequeue_cycle():
    shelter = AnimalShelter()
    cat1 = Cat()
    dog1 = Dog()
    cat2 = Cat()
    dog2 = Dog()
    cat3 = Cat()
    dog3 = Dog()

    # Enqueue the animals
    shelter.enqueue(cat1)
    shelter.enqueue(dog1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog2)
    shelter.enqueue(cat3)
    shelter.enqueue(dog3)

    shelter.dequeue("dog")
    shelter.dequeue("cat")
    shelter.dequeue("dog")
    shelter.dequeue("cat")
    shelter.dequeue("dog")
    shelter.dequeue("cat")

    shelter.enqueue(cat1)
    shelter.enqueue(dog1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog2)
    shelter.enqueue(cat3)
    shelter.enqueue(dog3)

    actual1 = shelter.dequeue("cat")
    actual2 = shelter.dequeue("dog")
    actual3 = shelter.dequeue("cat")
    actual4 = shelter.dequeue("dog")
    actual5 = shelter.dequeue("cat")
    actual6 = shelter.dequeue("dog")

    expected1 = cat1
    expected2 = dog1
    expected3 = cat2
    expected4 = dog2
    expected5 = cat3
    expected6 = dog3

    assert expected1 == actual1
    assert expected2 == actual2
    assert expected3 == actual3
    assert expected4 == actual4
    assert expected5 == actual5
    assert expected6 == actual6
