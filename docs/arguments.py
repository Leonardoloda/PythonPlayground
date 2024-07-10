import datetime


def log(message, level):
    print(f"{datetime.datetime.now()}    {level.upper()}: {message}")


log(message="Hello world", level="INFO")


# you can also use default values
def log_dev(message, level="debug"):
    print(f"{datetime.datetime.now()}    {level.upper()}: {message}")


# Now you don't need to passs that argument
log_dev(message="Hello world")


# Or you can have an endless amount of arguments, it will recieve a tuple with the arguments
def add(*args):
    print(f"Sum from {args[0]} to {args[-1]}")
    return sum(args)


# Now the function can receive and endless amount of arguments
total = add(1, 2, 3, 4, 5)

print(total)


# it can also be used with position arguments
def log_any(*messages, level):
    print(f"{datetime.datetime.now()}    {level.upper()}: {"".join(messages)}")


# positional arguments always need to go first
log_any("hello", " world", "!", level="warn")


# Same thin can be done to receive a dict instead of a tuple by using double **
def calculate(n, **kwargs):
    n = n + kwargs["add"]
    n = n * kwargs["multiply"]

    return n


# However it only works with positional argument
result = calculate(2, add=3, multiply=5)

print(f"Result: {result}")
