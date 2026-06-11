def even_count(numbers):
    evencount=0
    for i in numbers:
        if i%2==0:
            evencount=evencount+1
    return evencount
number_count=int(input("enter the number of values to be inputed in the list: "))
num=[]
for i in range(1,number_count+1):
    numb=int(input("enter a number: "))
    num.append(numb)
count_even=even_count(num)
print("the number of even numbers in the given list is ",count_even)
