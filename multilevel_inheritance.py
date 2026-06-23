# First parent class
class Flyer:
    def fly(self):
        return "I can fly high!"

# Second parent class
class Swimmer:
    def swim(self):
        return "I can swim deep!"

# Child class inheriting from both Flyer and Swimmer
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack quack!"

# Creating an instance of the child class
donald = Duck()

# Accessing methods from all classes
print(donald.quack())  # Output: Quack quack! (From Child)
print(donald.fly())    # Output: I can fly high! (From Parent1)
print(donald.swim())   # Output: I can swim deep! (From Parent2)