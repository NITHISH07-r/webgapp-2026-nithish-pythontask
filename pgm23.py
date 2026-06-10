set_A=set()
set_B=set()
count_a=int(input("enter the number of elements to be added: "))
for i in range(1,count_a+1):
    a=int(input("enter the value: "))
    set_A.add(a)
print(set_A)
count_b=int(input("enter the number of elements to be added: "))
for i in range(1,count_b+1):
    b=int(input("enter the value: "))
    set_B.add(b)
print(set_B)
if set_A.issubset(set_B):
    print("Set A is a subset of Set B")
else:
    print("Set A is not a subset of Set B")