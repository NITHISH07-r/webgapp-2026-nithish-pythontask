def greet(name, greeting="Hello"):
    return (f"{greeting}, {name}!")
print(greet("Alice"))    
print(greet("Bob", "Hi"))  

def add(a,b):
    c=a+b
    return c
print(add(1,2))