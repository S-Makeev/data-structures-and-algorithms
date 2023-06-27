from data_structures.queue import Queue
from data_structures.stack import Stack

class AnimalShelter:
    def __init__(self):
        self.animalQueue = Queue()

    def enqueue(self, animal):
        if isinstance(animal, (Dog, Cat)):
            self.animalQueue.enqueue(animal)

    def dequeue(self, pref):
        stack1 = Stack()
        stack2 = Stack()

        if pref != "dog" and pref != "cat":
            return None

        found_animal = None

        while not self.animalQueue.is_empty():
            animal = self.animalQueue.dequeue()

            if animal.name == pref:
                found_animal = animal
                break

            stack1.push(animal)

        while not stack1.is_empty():
            stack2.push(stack1.pop())

        while not stack2.is_empty():
            self.animalQueue.enqueue(stack2.pop())

        return found_animal


class Dog:
    def __init__(self):
        self.name = "dog"


class Cat:
    def __init__(self):
        self.name = "cat"
