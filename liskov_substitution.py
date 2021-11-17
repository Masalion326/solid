class Rectangle:  # 長方形

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def calcurate_area(self):
        return self._width * self._height


class Square(Rectangle):

    def __init__(self, size):
        self._width = self._height = size

    @Rectangle.width.setter
    def width(self, size):
        self._width = self._height = size

    @Rectangle.height.setter
    def height(self, size):
        self._width = self._height = size


def print_area(obj):
    change_to_width = 10
    change_to_height = 20
    obj.width = change_to_width
    obj.height = change_to_height
    if isinstance(obj, Square):
        change_to_width = change_to_height

    print('予想面積 = {}, 実際面積 = {}'.format(
        change_to_height * change_to_width,
        obj.calcurate_area()
    ))


rc = Rectangle(2, 3)
print_area(rc)

sq = Square(5)
print_area(sq)
