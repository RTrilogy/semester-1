# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

w = open("feep.pgm", "r")
data = w.readlines()
data = [line.strip().split() for line in data[1:]]
print(data)
w.close()
# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)