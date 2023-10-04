# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Usage
circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
