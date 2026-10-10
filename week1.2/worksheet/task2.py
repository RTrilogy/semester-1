# Worksheet 1.2: Task 2 Solution
from statistics import mean, median
import sys

try:
    numlist = input("Enter a sequence of float values: ")
except:
    sys.exit("Error: no numbers provided")

list1 = numlist.split(",")
floatlist = []
for i in list1:
    floatlist.append(float(list1[i]))

min_val = min(floatlist)
max_val = max(floatlist)
median_val = median(floatlist)
mean_val = mean(floatlist)

print(f"Minimum = {min_val}")
print(f"Maximum = {max_val}")
print(f"Mean = {mean_val}")
print(f"Median = {median_val}")

