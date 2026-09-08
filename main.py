# 1. Ask the user for at least 5 different inputs
name = input("Enter a name:\n")
place = input("Enter a place:\n")
adjective = input("Enter an adjective:\n")
animal = input("Enter an animal:\n")
verb = input("Enter a verb (past tense):\n")

# 2 & 3. Create an original story using all inputs and an f-string
# 4. Include quoted dialogue AND an escape character (\")
story = f"One day, {name} traveled to the {place} and encountered a very {adjective} {animal}. It {verb} right in front of them! {name} gasped and shouted, \"I can\'t believe my eyes!\""

# 5. Display the completed story
print("\nHere is your Mad Lib:")
print(story)