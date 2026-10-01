# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}")
#turns every character into lowercase
print(f"Modified String 2: {user_string.upper()}")
#turns every characters into upper case
print(f"Modified String 3: {user_string.strip()}")
#returns certains character stripped from the string
print(f"Modified String 4: {user_string.replace('a', '@')}")
#replaces a specified character within the string with another one
print(f"Modified String 5: {user_string.capitalize()}")
#turns the first character into upper case
print(f"Modified String 6: {user_string[::-1]}")
#reverses the string by starting at the end and finishing at the start
print(f"Modified String 7: {user_string.title()}")
#turns every new word initial character into upper case
print(f"Modified String 8: {len(user_string)}")
#returns the length of the string
print(f"Modified String 9: {user_string.find('a')}")
#returns the index of a certain character in the string
print(f"Modified String 10: {user_string.count('a')}")
#returns the amount of times a character is found in the string
print(f"Modified String 11: {user_string.startswith('Hello')}")
#returns true or false depending on if the string begins with a specified collection of characters
print(f"Modified String 12: {user_string.endswith('!')}")
#returns true or false depending on if the string ends with a specified collection of characters
print(f"Modified String 13: {user_string.isalnum()}")
#returns true or false depending on if the string contains alphabetically rising characters and 0-9 digits 
print(f"Modified String 14: {user_string.isalpha()}")
#returns true or false depending on if the string characters rise alphabetically
print(f"Modified String 15: {user_string.isdigit()}")
#returns true or false depending on if the string contains only digits



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!