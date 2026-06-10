str=input("enter a string: ")
print(len(str))
rep_count=0
rep=input("enter a character to find its occurence: ")
for i in str:
    if i in rep:
        rep_count=rep_count+1
print(rep_count)



