# See README.md for instructions on what to do this program

import random

#random.seed(15)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)
#whenever the program is called without random.seed, it egenrates a random seed for the program to generate the numbers, yet with random.seed
#it applies a seed to the program so the random numbers are always the same upon running