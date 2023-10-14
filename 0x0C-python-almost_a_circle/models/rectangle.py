#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """inherites the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance method for the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """string representation of the rectangle class"""
        m = "[Rectangle] ({}) {}/{} - {}/{}"
        return m.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """hight setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets y value"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """prints the rectangle with the symbol #"""
        rectangle = []

        print("\n" * (self.__y), end="")
        for _ in range(self.__height):
            rectangle.extend([" " * self.__x, "#" * self.__width, '\n'])
        print("".join(rectangle), end="")

    def update(self, *args, **kwargs):
        """
        update the rectangle with args and kwargs
        """
        length = len(args)

        try:
            if (length > 0):
                raise ValueError
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        except ValueError:
            if (length == 1):
                self.id = args[0]
            elif (length == 2):
                self.id, self.width = args
            elif (length == 3):
                self.id, self.width, self.height = args
            elif (length == 4):
                self.id, self.width, self.height, self.x = args
            elif (length == 5):
                self.id, self.width, self.height, self.x, self.y = args

    def to_dictionary(self):
        """convert rectangle instance to dictionary"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
