# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!

class Circle(Shape):
    def __init__(self, radius):
        super.__init_((4,5), "red")
        self.rad = radius

    def set_radius(self, num):
        if not isinstance(num, int) or not isinstance(num, float):
            raise TypeError("You are supposed to enter a number.")
        if num <= 0:
            raise ValueError("Should be higher than 0.")

        self.rad = num

    def area(self):
        return ( self.rad ** 2 ) * 3.14

    def perimeter(self):
        return ( self.rad * 2 ) * 3.14