class Organism:
    alive = True


class animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.bark())