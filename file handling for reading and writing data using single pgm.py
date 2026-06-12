#write data
with open("sample.txt","w") as file:
    file.write("name:John\n")
    file.write("age:20\n")

#read data
with open("sample.txt","r") as file:
    print(file.read())