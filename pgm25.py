a=input("enter the scale in which temperature is given: ")
b=input("enter the scale in which temperature is to be changed: ")
c=int(input("enter the temperature value: "))
if a=="celsius" or a=="Celsius" or a=="CELSIUS" and b=="fahrenheit" or b=="Fahrenheit" or b=="FAHRENHEIT":
    d=(c*(9/5))+32
    print("temperature in fahrenheit from celsius: ",d)
elif a=="fahrenheit" or a=="Fahrenheit" or a=="FAHRENHEIT" and b=="celsius" or b=="Celsius" or b=="CELSIUS":
    d=(c-32)*(5/9)
    print("temperature in celsius from fahrenheit: ",d)
elif a=="celsius" or a=="Celsius" or a=="CELSIUS" and b=="kelvin" or b=="Kelvin" or b=="KELVIN":
    d=c+273.15
    print("temperature in kelvin from celsius: ",d)
elif a=="kelvin" or a=="Kelvin" or a=="KELVIN" and b=="celsius" or b=="Celsius" or b=="CELSIUS":
    d=c-273.15
    print("temperature in celsius from kelvin: ",d)
elif  a=="fahrenheit" or a=="Fahrenheit" or a=="FAHRENHEIT" and b=="kelvin" or b=="Kelvin" or b=="KELVIN":
    d=((c-32)*(5/9))+273.15
    print("temperature in kelvin from fahrenheit: ",d)
elif a=="kelvin" or a=="Kelvin" or a=="KELVIN" and b=="fahrenheit" or b=="Fahrenheit" or b=="FAHRENHEIT":
    d=(((c-273.5)*(9/5))+32)
    print("temperature in fahrenheit from kelvin: ",d)
else:
    print("enter proper data")