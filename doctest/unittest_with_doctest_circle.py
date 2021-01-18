import math

class Circle:

    def __init__(self, radius):

        """
        >>> c1 = Circle(2.5)
        >>> c1.radius
        2.5
        """
        self.radius = radius

    def area(self):

        """
        >>> c1 = Circle(2.5)
        >>> c1.area()
        19.63

        """

        return round(math.pi*(self.radius**2),2)