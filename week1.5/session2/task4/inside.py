# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import Circle, Point

p1 = Point(100,100)
c1 = Circle(7, (5,6))

if p1 in c1:
    print("point is inside circle!")