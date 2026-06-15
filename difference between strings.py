str=input().split()
s1=str[0]
s2=str[1]
difference=" "
for i in s1:
    if i not in s2:
        difference+=i
if difference=="":
    print("no different values found")
else:
    print(difference)

