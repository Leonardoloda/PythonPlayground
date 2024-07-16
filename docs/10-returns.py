# Functions with returns

# Functions can return any kind of value
def add(a, b):
  return a + b

a = 1
b = 2
c = add(a, b)

print(c)

def format_name(first_name, last_name):
  """Format a name into title case"""
  return f"{first_name} {last_name}".title()

print(format_name("leo", "leo"))

# Calculator

print("""
   ___  _     __   ___        __   _  _____  ___  __  
  / __\/_\   / /  / __/\ /\  / /  /_\/__   \/___\/__\ 
 / /  //_\\ / /  / / / / \ \/ /  //_\\ / /\//  // \// 
/ /__/  _  / /__/ /__\ \_/ / /__/  _  / / / \_// _  \ 
\____\_/ \_\____\____/\___/\____\_/ \_\/  \___/\/ \_/ 
                                                      
""")


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator(number1 = None):
  keep_calculating = True

  if number1 == None:
    number1 = int(input("What's the first number? "))
  
  while keep_calculating:
    operation = input("Enter the operation: ")
    number2 = int(input("Enter the second number: "))
  
    if operation in operations:
      result = operations[operation](number1, number2)
      print(f"{number1} {operation} {number2} = {result}")
    else: 
      print("You have entered an invalid operation")
  
    number1 = result
    choice = input("Would you like to continue calculating? Type 'y' for yes or 'n' for no: ")
  
    if choice == "y":
      calculator(number1)
    else:
      return

calculator()