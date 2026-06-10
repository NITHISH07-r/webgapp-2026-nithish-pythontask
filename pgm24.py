val1=int(input("enter a number: "))
val2=int(input("enter a number: "))
operation=input("enter the operation to be performed: ")
if operation=="addition" or operation=="Addition" or operation=="ADDITION" or operation=="+":
    c=val1+val2
    print("sum= ",c)
elif operation=="subtraction" or operation=="Subtraction" or operation=="SUBTRACTION" or operation=="-":
    c=val1-val2
    print("difference= ",c)
elif operation=="multiplication" or operation=="Multiplcation" or operation=="MULTIPLICATION" or operation=="*":
    c=val1*val2
    print("product: ",c)
elif operation=="division" or operation=="Division" or operation=="DIVISION" or operation=="/":
    c=val1/val2
    print("quotient= ",c)
else:
    print("operation not found")
