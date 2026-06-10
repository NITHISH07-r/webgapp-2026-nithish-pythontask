print("Hello, World!")
s="hello"
print(s.upper())
print(s.lower())
print(s+" name")
print(s.replace("e","o"))
print(len(s))

marks=int(input("enter marks: "))
if marks>=90:
    print("grade A")
elif marks <90 and marks >= 75:
    print("grade B")
elif marks <75 and marks >=50:
    print("grade C")
else:
    print("grade D")


age=int(input("AGE: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")


name=input("Enter your name: ")
c=len(name)
if c>=7:
    print("your name is too long")
elif c<=4:
    print("your name is too short")
else:
    print("your name is in correct length")