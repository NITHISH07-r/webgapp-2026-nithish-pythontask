str=input("Enter a string: ")
odd=" "
even=" "
output=" "
for index,value in enumerate(str,start=1):
    if index %2 == 0:
        even=even+value
    else:
        odd=odd+value
output=f"{odd} {even}"
print(output)

