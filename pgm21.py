import operator
dict1={}
dict1_count=int(input("enter the number of values to store in dict1: "))
for i in range(1,dict1_count+1):
    key=input("enter the key: ")
    value=input("enter the value: ")
    dict1[key]=value
print(dict1)
sorted_dict1=dict(sorted(dict1.items(),key=operator.itemgetter(1)))
print(sorted_dict1)