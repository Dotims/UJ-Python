import unittest

from points import Point


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[{}, {}]".format(self.pt1, self.pt2)

    def __repr__(self):
        return "Rectangle({}, {}, {}, {})".format(
            self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2,
                     (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r = Rectangle(1, 2, 5, 4)
        self.square = Rectangle(-1, -1, 1, 1)

    def test_str_repr(self):
        self.assertEqual(str(self.r), "[(1, 2), (5, 4)]")
        self.assertEqual(str(self.square), "[(-1, -1), (1, 1)]")
        self.assertEqual(repr(self.r), "Rectangle(1, 2, 5, 4)")
        self.assertEqual(repr(self.square), "Rectangle(-1, -1, 1, 1)")

    def test_eq_ne(self):
        self.assertTrue(self.r == Rectangle(1, 2, 5, 4))
        self.assertFalse(self.r == self.square)
        self.assertFalse(self.r == Rectangle(1, 2, 5, 5))
        self.assertTrue(self.r != self.square)
        self.assertFalse(self.r != Rectangle(1, 2, 5, 4))
        self.assertFalse(self.r == "Rectangle(1, 2, 5, 4)")

    def test_center(self):
        self.assertEqual(self.r.center(), Point(3, 3))
        self.assertEqual(self.square.center(), Point(0, 0))
        self.assertEqual(Rectangle(0, 0, 1, 3).center(), Point(0.5, 1.5))

    def test_area(self):
        self.assertEqual(self.r.area(), 8)
        self.assertEqual(self.square.area(), 4)
        self.assertEqual(Rectangle(0, 0, 0.5, 4).area(), 2)
        self.assertEqual(Rectangle(2, 2, 2, 7).area(), 0)

    def test_move(self):
        self.r.move(2, -3)
        self.assertEqual(self.r, Rectangle(3, -1, 7, 1))
        self.assertEqual(self.r.area(), 8)
        self.assertEqual(self.r.center(), Point(5, 0))
        self.square.move(0, 0)
        self.assertEqual(self.square, Rectangle(-1, -1, 1, 1))
        self.square.move(1.5, 1)
        self.assertEqual(self.square, Rectangle(0.5, 0, 2.5, 2))


if __name__ == "__main__":
    unittest.main()
