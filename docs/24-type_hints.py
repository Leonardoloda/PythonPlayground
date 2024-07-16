# Python allows you to add type hints they will warn you when they expect a certain type

age: int

# Although it doesn't give an error when running, shows a warning
age = "20"

print(age)


# can also be done with functions, and you can specify a return type
def add(n1: int, n2: int) -> int:
    return n1 + n2


add(1, 2)

add("True", 2)
