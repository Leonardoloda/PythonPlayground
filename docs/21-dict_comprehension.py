# Similar to list comprehension, you can do it iwth dicts
from random import randrange

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

names_with_scores = {name: randrange(0, 100) for name in names}

print(f"Dict with names and scores {names_with_scores}")

short_names_with_scores = {name: randrange(0, 100) for name in names if len(name) <= 4}

print(f"Dict with short names with scores {short_names_with_scores}")

# it can be used to iterate over other dicts
passed_students = {name: names_with_scores[name] for name in names_with_scores if names_with_scores[name] >= 70}

print(f"Dict with students with passing scores {passed_students}")

# you can also use a different for
curved_students = {name: score for (name, score) in names_with_scores.items() if score > 60 and score < 70}

print(f"Dict with names with average scores {curved_students}")
