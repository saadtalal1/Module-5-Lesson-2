import math

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return math.pi * (self.radius ** 2)

    def circle_perimeter(self):
        return 2 * math.pi * self.radius


my_circle = Circle(5)
print("Radius:    ", my_circle.radius)
print("Area:      ", my_circle.circle_area())
print("Perimeter: ", my_circle.circle_perimeter())
