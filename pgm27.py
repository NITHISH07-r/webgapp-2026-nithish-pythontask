def add(*args):
    total=0
    for i in args:
        total=total+i
    return total
print(add(10,20,30,40,50,60))