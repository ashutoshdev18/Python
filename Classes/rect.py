class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        print("getting width")
        return self._width
    
    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("width must be greater than 0")
        self._width = width
        
    @property
    def height(self):
        print("getting height")
        return self._height
    
    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("height must be greater than 0")
        self._height = height
    
    def area(self):
        return self._width * self._height
    def perimeter(self):
        return 2 * (self._width + self._height)
    def __str__(self):
        return 'Rectangle: _width={0}, _height={1}, area={2}, perimeter={3}'.format(self._width, self._height, self.area(), self.perimeter())
    
r1 = Rectangle(10, 20)
print(r1.width)
print(r1.height)

r2 = Rectangle(100, 200)
print("R1 is ",r1)
print("R2 is ",r2)
