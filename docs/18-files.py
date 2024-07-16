# You can open files with the open command

file = open("./files/sample.txt")

# You can read the content from the file
content = file.read()

# Now you can access the content
print(content)

# We have to make sure to close the file to keep performance
file.close()

# To avoid opening an closing connections, you can use with  to open and close automatically
with open("./files/sample.txt") as file_with:
    content = file_with.read()
    print(content)

# You can also use it to write bt you need to set the permission

with open("./files/sample.txt", mode="w") as file_with:
    new_text = "Hello World! was updated"

    # This replaces the current text
    file_with.write(new_text)

# You can use the append mode to add new content
with open("./files/sample.txt", mode="a") as file_append:
    new_text = "\n Previous Hello World! wasn't replaced"

    file_append.write(new_text)

# If the file doesn't exit, it gets created
with open("./files/sample_unexisting.txt", mode="w") as file_create:
    new_text = "Hello World! was created into a new file"

    file_create = file_create.write(new_text)
