# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        """
        Initializes the class with a date of birth and name attribute.
        """

        if not isinstance(name, str):
            raise TypeError("Name should be a string.")
        if name == "":
            raise ValueError("Name should not be an empty string.")
        if not isinstance(birth, date):
            raise TypeError("Date of birth should be a date")

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        """
        Returns the initials of the name of the object in uppercase
        """
        name2 = self.name.split()
        a2 = []
        for i in name2:
            a2.append(i[0].upper())
        return "".join(a2)
        
    def is_birthday(self):
        """
        Returns true or false depending on if today's date is equal to the object's birthday
        """

        if self.birth.month == date.today().month and self.birth.day == date.today().day:
            return True
        else:
            return False

