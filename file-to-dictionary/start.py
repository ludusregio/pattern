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

filename = "./natural_world.txt"

with open(filename, "w") as f:
    f.writelines([f'{creature}\n' for creature in creatures])

# You should not need to modify the code above this line
# Start to write your code below this line

# Use variable filename the file







# You should not modify the code below this line
os.remove(filename)
