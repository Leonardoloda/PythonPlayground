from time import sleep


# decorators are functions that wrap another function to give it extra functionality

def delay(func):
    def wrapper(*args, **kwargs):
        sleep(2)
        func(*args, **kwargs)

    return wrapper


def greeting(name):
    print(f"Hello {name}")


@delay
def greeting_delayed(name):
    print(f"Hello {name}")


greeting_delayed('John')
greeting('John')


# They can modify the input or output
def scream(func):
    def wrapper(name: str):
        func(name.upper())

    return wrapper


@scream
def salute(name):
    print(f"Hello {name}")


salute("leo")

# You could also avoid teh syntactical sugar and jus create the decorated function
yell_ugly = scream(salute)
yell_ugly("Rodolfo")


# Plus you can use multiple decorators on a function
@scream
@delay
def yell_delayed(name: str):
    print(f"Hello {name}")


yell_delayed('Jaime')
