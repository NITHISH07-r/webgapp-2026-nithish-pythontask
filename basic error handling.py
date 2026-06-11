try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"10 / {num} = {result}")

except ValueError:
    print("Not a valid number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

except Exception as e:
    print(f"Error: {e}")

else:              
    print("Success!")

finally:          
    print("Done.")
    