a=input("enter the scale in which temperature is given: ")
b=input("enter the scale in which temperature is to be changed: ")
c=int(input("enter the temperature value: "))
if (a.lower() == "celsius") and (b.lower() == "fahrenheit"):
    d = (c * (9/5)) + 32
    print("temperature in fahrenheit from celsius:", d)

elif (a.lower() == "fahrenheit") and (b.lower() == "celsius"):
    d = (c - 32) * (5/9)
    print("temperature in celsius from fahrenheit:", d)

elif (a.lower() == "celsius") and (b.lower() == "kelvin"):
    d = c + 273.15
    print("temperature in kelvin from celsius:", d)

elif (a.lower() == "kelvin") and (b.lower() == "celsius"):
    d = c - 273.15
    print("temperature in celsius from kelvin:", d)

elif (a.lower() == "fahrenheit") and (b.lower() == "kelvin"):
    d = ((c - 32) * (5/9)) + 273.15
    print("temperature in kelvin from fahrenheit:", d)

elif (a.lower() == "kelvin") and (b.lower() == "fahrenheit"):
    d = ((c - 273.15) * (9/5)) + 32
    print("temperature in fahrenheit from kelvin:", d)

else:
    print("enter proper data")
