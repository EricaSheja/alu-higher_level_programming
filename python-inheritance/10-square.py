#!/usr/bin/python3
# Square inherits from Rectangle
# print() still shows [Rectangle] because we don't override __str__
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        # Validate size using the inherited integer_validator method
        self.integer_validator("size", size)

        # Store size as a private attribute
        self.__size = size

        # Call Rectangle's __init__ with size for both width and height
        super().__init__(size, size)

    def area(self):
        # Area = size x size
        return self.__size * self.__size
