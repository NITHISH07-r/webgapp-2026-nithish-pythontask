def my_func(**details):
    for key,value in details.items():
        print(key,":",value)
my_func(name="ram",age=25,Place="Madurai")