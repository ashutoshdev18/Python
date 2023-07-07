class Rectangle:

    def __init__(self, _width, _height):
        self._width = _width
        self._height = _height
    def get_width(self):
        return self._width
    def set_width(self, width):
        if width < 0:
            raise ValueError('Width must be positive')
        self._width = width
    def area(self):
        return self._width * self._height
    def perimeter(self):
        return 2 * (self._width + self._height)
    def __str__(self):
        return 'Rectangle: _width={0}, _height={1}, area={2}, perimeter={3}'.format(self._width, self._height, self.area(), self.perimeter())
    def __eq__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        return NotImplemented


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
# print("R1 is R2 {0}".format(r1 is r2))
# print("R1 == R2 {0}".format(r1 == r2)) # calls the __eq__ operator.

# print("R1 == 100 {0}".format(r2 == 100)) # will throw error as R1 and 100 are different types. to avoid this error if it is instance.
# print("R1 < R2 {0}".format(r1 < r2))
# print("R1 < 100 {0}".format(r1 <= 100))

# r1.__width = 200
# print(r1.get__width())
print(r1)
print(r1.get_width())
print(r1.set_width(20))
print(r1.get_width())

#getters and setters for security