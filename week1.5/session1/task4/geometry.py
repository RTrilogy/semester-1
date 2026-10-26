# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
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

# Add a definition for a Circle class here, giving it
class Circle():
      def __init__(self, centre, radius):
            self.centre = centre
            self.radius = radius

        def area(self):
            area1 = ( self.radius ^ 2 ) * 3.14
            return round(area1, 2)

        def perimeter(self):
            perimeter1 = 3.14 * ( self.radius * 2 )
            return round(perimeter1, 2)

#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
