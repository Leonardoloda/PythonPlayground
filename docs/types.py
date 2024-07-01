# Python has the basic types

# Strings
string = "Sample"
print(string, type(string))

parsed_string = str(1234)
print(parsed_string, type(parsed_string))

# Integers
number = 1_072_709_315
print(number, type(number))
parsed_number = int(number)
print(parsed_number, type(parsed_number))

boolean = True
print(boolean, type(boolean))
# Doesn't parse, just check for falsy values
parsed_boolean = bool(None)
print(parsed_boolean, type(parsed_boolean))

floatType = 3.14159
print(type(floatType))

# operation are the same shit
number1 = 10
number2 = 5

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(number1**number2)  # Exponentials do change

# numbers can also be rounded
print("round(pi, 2)", round(3.1459, 2))

# division can automatically floor
print("8 // 3", 8 // 3)

# string can use template literals as f strings
print(f"Your score is {number1}")

# Tip calculator
print("Welcome to the tip calculator.")
bill = input("What wass the total bill? $")
tip = input("Would you like to give 10, 12, or 15% tip? ")
people = input("How many people to split the bill? ")

total_bill = float(bill) + (float(bill) * (float(tip) / 100))

print(f"The total for the bil is {total_bill}")
print(f"Each person should pay: ${round(total_bill / int(people), 2)}")
