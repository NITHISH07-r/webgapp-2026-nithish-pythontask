# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Derived class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} barks!")

# Further derived class (inherits from Dog)
class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age

    def speak(self):
        print(f"{self.name} the {self.breed} puppy (age {self.age}) yelps!")


animal = Animal("Generic Animal")
animal.sound()

dog = Dog("Buddy", "Golden Retriever")
dog.bark()

puppy = Puppy("Charlie", "Golden Retriever", 1)
puppy.speak()
