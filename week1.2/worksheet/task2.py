# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys


floatlist = read_numbers()
if floatlist == []:
    print("Error: no numbers provided")
    sys.exit("Error: no numbers provided")


min_val = min(floatlist)
max_val = max(floatlist)

sortlist = sorted(floatlist)
odd = False
if (len(floatlist) % 2) == 0:
    odd = False
else:
    odd = True
if odd:
    median_val = sortlist[len(floatlist) // 2]
else:
    median_val = ( ( sortlist[len(floatlist) // 2] - sortlist[(len(floatlist) // 2) - 1] ) / 2 ) + sortlist[(len(floatlist) // 2) - 1]

num1 = 0.0
for i in range(len(floatlist)):
    num1 = num1 + floatlist[i]
num1 = num1 / len(floatlist)
mean_val = num1

print(f"Minimum = {min_val}")
print(f"Maximum = {max_val}")
print(f"Mean = {mean_val}")
print(f"Median = {median_val}")

