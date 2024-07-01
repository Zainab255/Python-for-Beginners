num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive")
    # Perform some action for positive number
    # Example: print the square of the number
    print("Square of the number is:", num ** 2)
elif num < 0:
    print("The number is negative")
    # Perform some action for negative number
    # Example: print the absolute value of the number
    print("Absolute value of the number is:", abs(num))
else:
    print("The number is zero")



# (i)

def perform_operations_positive(number):
    if 10 <= number <= 20:
        print(f"The power of {number} is {number ** 2}")
    elif 20 < number <= 30:
        print(f"The square of {number} is {number ** 2}")
    elif number > 30:
        print("YourName " * (number // 2))

# Test cases
perform_operations_positive(15)  # The power of 15 is 225
perform_operations_positive(25)  # The square of 25 is 625
perform_operations_positive(35)  # YourName repeated 17 times


# (ii)
def perform_operations_negative(number):
    if -20 <= number < -10:
        print("Pattern for -10 to -20:")
        print("  *")
        print(" ***")
        print("*****")
        print(" ***")
        print("  *")
    elif -30 <= number < -20:
        print("Pattern for -20 to -30:")
        print("  *")
        print(" ***")
        print("*****")
    elif number < -30:
        print("YourDepartmentName")

# Test cases
perform_operations_negative(-15)  # Pattern for -10 to -20
perform_operations_negative(-25)  # Pattern for -20 to -30
perform_operations_negative(-35)  # YourDepartmentName
