# Function to calculate average
def average(numbers):
    total=sum(numbers)     
    count=len(numbers)      
    return total / count       
n = int(input("enter the number of values to be given as input: "))
values=[]
for i in range(n):
    num=float(input("enter the value: "))
    values.append(num)
avg=average(values)
print("The average of the given numbers is: ",avg)

