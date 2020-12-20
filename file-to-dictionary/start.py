import uuid
import os

creatures = [
        "Pinguin",
        "Seal",
        "Moose",
        "Dog",
        "Elephant",
        "Sloth",
        "Gorilla",
        "Giraffe",
        "Polar Bear",
        "Platypus",
        "Orca",
        "Whale",
        "Squirel",
        "Mouse",
        "Meerkat",
        "Flamingo"
        ]

filename = str(uuid.uuid4().hex)

with open(filename, "w") as f:
    f.writelines([f'{creature}\n' for creature in creatures])

# You should not need to modify the code above this line
# Start to write your code below this line

# Use variable filename the file





# Do not remove below code
os.remove(filename)
