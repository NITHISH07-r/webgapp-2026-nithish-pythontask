dict1={}
dict2={}
dict1_count=int(input("enter the number of values to store in dict1: "))
for i in range(1,dict1_count+1):
    key=input("enter the key: ")
    value=input("enter the value: ")
    dict1[key]=value
print(dict1)
dict2_count=int(input("enter the number of values to store in dict2: "))
for i in range(1,dict2_count+1):
    key=input("enter the key: ")
    value=input("enter the value: ")
    dict2[key]=value
print(dict2)
dict1.update(dict2)
print("combine_dict: ",dict1)

