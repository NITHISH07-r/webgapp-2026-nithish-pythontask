list1=[2,1,3,4,2,3,4]
listnew=[]
for i in list1:
    if i in listnew:
        pass
    else:
        listnew.append(i)
print(listnew)