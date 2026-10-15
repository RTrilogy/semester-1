# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.
salut = input("ENTER THE NAME OF dA FILE U WANNA READ LOL: ") + ".txt"

# open and read the file
dante = open(salut, "r")
values = dante.readlines()
data = [line.strip().split() for line in values]
newlist = []
for p in data:
    for x in p:
        newlist.append(x)

print(len(newlist))
dante.close()

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210