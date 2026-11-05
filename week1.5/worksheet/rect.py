# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Must be an integer.")
        if width <= 0 or height <= 0:
            raise ValueError("Both values must be higher than 0.")

        self.width = width
        self.height = height


    def is_square(self):
        """
        Checks if the object width and height are equal, creating a square.
        """
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        """
        Multiplies the width by the height to return the area of the object.
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Adds every side of the rectangle together, returning the perimeter of the object.
        """
        return (self.width * 2) + (self.height * 2)

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
