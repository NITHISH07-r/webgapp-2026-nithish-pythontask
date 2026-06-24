# Simple Error Handling Example

try:
    # Input from user
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    # Division operation
    result = num1 / num2
    print("Result:", result)

except ValueError:
    # Handles invalid input (like entering letters instead of numbers)
    print("Error: Please enter valid integers.")

except ZeroDivisionError:
    # Handles division by zero
    print("Error: Division by zero is not allowed.")

finally:
    # Always executes, whether error occurs or not
    print("Program execution completed.")
