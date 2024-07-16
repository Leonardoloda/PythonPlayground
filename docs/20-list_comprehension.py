# So far list have been created using for loops
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_easy = [n for n in range(10)]

new_list = []

for number in numbers:
    new_list.append(number)

# however list comprehensions allows us to shorten the syntax
new_list_short = [n for n in numbers]

print(f"List created with list comprehension {new_list_short}")

# it contains 2 parts: the condition for the new number and the for
new_list_double = [n * 2 for n in numbers]

print(f"List with double the value {new_list_double}")

new_list_plus = [n + 1 for n in numbers]

print(new_list_plus)

# works with other form of for
empty_list = ["" for i in range(10)]

print(empty_list)

none_list = [None for i in range(10)]

print(none_list)

list_odd = [n for n in range(1, 10, 2)]

print(f"List with odd numbers: {list_odd}")

list_even = [n for n in range(0, 11, 2)]

print(f"List with even numbers: {list_even}")

# Also works for other types
name = "Angela"

letter_list = [letter for letter in name]

print(f"List with letters from word {letter_list}")

# there's a 3rd part that allows you to use a condition

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) <= 4]

print(f"List with short names: {short_names}")

uppercase_names = [name.upper() for name in names if len(name) > 4]

print(f"List with uppercase letters: {uppercase_names}")
