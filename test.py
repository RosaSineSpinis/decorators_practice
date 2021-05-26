class Circle:
    def __init__(self, radius):
        self._radius = radius


    @property
    def radius(self):
        """Get value of radius"""
        return self._radius


    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

c = Circle(5)
c.radius


c.radius = 2
c.radius = -2

