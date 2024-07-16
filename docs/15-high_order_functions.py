def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# High order functions exists as function that use another function to execute
# It can receive it as a parameter or returns it
def calculate(n1, n2, operation):
    return operation(n1, n2)


# Functions can be passed as arguments
print(calculate(2, 3, add))
print(calculate(2, 3, subtract))
print(calculate(2, 3, multiply))
print(calculate(2, 3, divide))
