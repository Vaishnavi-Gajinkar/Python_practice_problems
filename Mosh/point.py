class Point():
    def calcDist(self):
        return ("Calculated distance btwn 2 points is: ")
    def move(self):
        return ("Move coordinates to ")

print(Point.calcDist())
print(Point.move())
# print(Point.x)
# print(Point.y)
point1 = Point()
point1.a = 45
point1.b = 90

Point.x = 10
Point.y = 11

print(f'X coordinate is {Point.x} and Y coordinate is {Point.y}')
print(f'Angles made are {point1.a} and {point1.b}')