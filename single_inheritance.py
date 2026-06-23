# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent constructor using super()
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} barks!")

# Create objects
animal = Animal("Generic Animal")
animal.speak()

dog = Dog("Buddy", "Golden Retriever")
dog.speak()