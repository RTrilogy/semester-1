# Worksheet 1.2: Task 1 Solution
import sys

try:
    num1 = int(input("Enter your grade as an integer between 0 and 100: "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if num1 >= 0 and num1 <= 39:
    print(f"{num1} is a Fail")
elif num1 >= 40 and num1 <= 69:
    print(f"{num1} is a Pass")
else:
    print(f"{num1} is a Distinction")