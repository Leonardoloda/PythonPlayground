"""
# Opening a file not existing can cause a FileNotFound error
with open("files/unexisting.txt") as file:
    print("Works")


# Key Error
custom_dict = {
    "key":"value"
}

print(custom_dict["key_1"])

# Index error 
numbers = [0, 1, 2]

print(numbers[5])

# TypeError
print("abc" + 5)
"""

# Exceptions can be catched with a try catch block
try:
    result = "abc" + 5
except:
    print("Error happened")
finally:
    print("Finalaly convert it")
    print("abc" + str(5))


# However you should be specific about the exceptions being catched
try:
    file = open("files/unexisting.txt")
    custom_dict = {"key": "value"}
    print(custom_dict["key1"])

except FileNotFoundError as message:
    print("WARN - Failed to open the file", message)

    file = open("files/unexisting.txt", mode="w", encoding="utf-8")

# You can also receive the initial message
except KeyError as error_message:
    print("ERR - Not existing key", error_message)

# If it works, we can just put the rest of the code in the else
else: 
    content = file.read()
    print(content)

# Finally allolws you to execute no mather what happened
finally:
    print("Close the file")
    file.close()

# Errors can also be raised manually
def add(n1, n2):
    """ Adds 2 numbers """

    if not isinstance(n1, int):
        raise TypeError("Invalid type in n1")
    
    if not isinstance(n2, int):
        raise TypeError("Innvalid type in n2")
    
    return n1 + n2

try:
    result = add("5", 3)
except TypeError as message:
    print(f"Error: {message}")
finally:
    result = add(5,3)
    print(result)