class Circle:
    def __init__(self, radius):
        print("object is created radius= ", radius)
        self.radius = radius

    @property
    def radius_radius(self):
        print("radius property is working ")
        """get value of radius property is set or get I think"""
        return self.radius + self.radius

    @radius_radius.setter
    def radius_radius(self, value):
        """Set radius, raise error if negative"""
        print("setter is working ")
        if value >= 0:
            print("we are in if ")
            self.radius = value
        else:
            raise ValueError("Radius must be positive")

    @radius_radius.deleter
    def radius_radius(self):
        """Set radius, raise error if negative"""
        print("deleter is working ")
        self.radius = None


    @classmethod
    def area(cls, value):
        """freerly connected with the class, it is more like reuse of constructor, used only with class_name.method"""
        print("area classmethod  ")
        return cls(value)

    @staticmethod
    def pi():
        """freerly connected with the class, acess obj.method or class_name.method"""
        return 3.14

obj1 = Circle(10)

obj1.radius_radius = 5
print(obj1.radius_radius)

# obj1.radius_radius = -5
# print(obj1.radius_radius)

del obj1.radius_radius
print(obj1.radius)

obj1 = Circle.area(10)

print(obj1.radius)