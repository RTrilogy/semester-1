import random

# Get user to input how many random numbers they want
numof = int(input("how many random numbers"))
numlist = []

# Generate this many random numbers
for i in range(0, numof):
    num = random.randint(1, 10000)
    numlist.append(num)

# Write the random numbers to a file named random.txt, one number per line
file = open("random.txt", "a")
for i in numlist:
    file.write(f"{i}\n")
file.close()
