import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

listword = []

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
numof = int(input("how many random choices"))
for i in range(0, numof):
    word = random.choice(names)
    if word not in listword:
        listword.append(word)
        print(word)



# Display the chosen names, one per line
