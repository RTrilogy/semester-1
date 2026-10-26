# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
            """
            Creates a Point, given x & y coordinates.
            """
            self.x = x_coordinate
            self.y = y_coordinate
    

    # Add distance() method here
    def distance(self):
          return round(math.hypot(self.x, self.y), 2)

    # Add distance_to() method here
    def distance_to(self, point1):
          distanceval = point1.distance() - self.distance()
          return round(distanceval, 2)
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
p1 = Point(2, 6)
p2 = Point( 9, 4)
print(p1.x)
print(p2.y)
print(p1.distance())
print(p2.distance())
print(p1.distance_to(p2))