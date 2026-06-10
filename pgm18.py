num=[]
count=int(input("enter number of elements to be inserted in the list: "))
for i in range(1,count+1):
    a=int(input(""))
    num.append(a)
print(num)
even_count=0
odd_count=0
for i in num:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("number of even digits: ",even_count)
print("number of odd digits: ",odd_count)