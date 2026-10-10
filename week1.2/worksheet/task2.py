# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

try:
    floatlist = read_numbers()
except:
    sys.exit("Error: no numbers provided")

min_val = min(floatlist)
max_val = max(floatlist)

sortlist = floatlist.sort()
median_val = floatlist[len(floatlist) // 2]

num1 = 0.0
for i in range(len(floatlist)):
    num1 = num1 + floatlist[i]
num1 = num1 / len(floatlist)
mean_val = num1

print(f"Minimum = {min_val}")
print(f"Maximum = {max_val}")
print(f"Mean = {mean_val}")
print(f"Median = {median_val}")

