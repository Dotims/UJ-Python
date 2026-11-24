import math
import unittest


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p = Point(1, 2)
        self.q = Point(3, -4)

    def test_str_repr(self):
        self.assertEqual(str(self.p), "(1, 2)")
        self.assertEqual(str(self.q), "(3, -4)")
        self.assertEqual(repr(self.p), "Point(1, 2)")
        self.assertEqual(repr(Point(0.5, 0)), "Point(0.5, 0)")

    def test_eq_ne(self):
        self.assertTrue(self.p == Point(1, 2))
        self.assertFalse(self.p == self.q)
        self.assertFalse(self.p == Point(2, 1))
        self.assertTrue(self.p != self.q)
        self.assertFalse(self.p != Point(1, 2))
        self.assertTrue(Point(2, 0) == Point(2.0, 0.0))
        self.assertFalse(self.p == (1, 2))
        self.assertTrue(self.p != (1, 2))

    def test_add_sub(self):
        self.assertEqual(self.p + self.q, Point(4, -2))
        self.assertEqual(self.q + self.p, Point(4, -2))
        self.assertEqual(self.p - self.q, Point(-2, 6))
        self.assertEqual(self.q - self.p, Point(2, -6))
        self.assertEqual(self.p - self.p, Point(0, 0))
        self.assertEqual(self.p, Point(1, 2))

    def test_mul(self):
        self.assertEqual(self.p * self.q, -5)
        self.assertEqual(self.q * self.p, -5)
        self.assertEqual(self.p * Point(2, -1), 0)
        self.assertEqual(self.p * self.p, 5)

    def test_cross(self):
        self.assertEqual(self.p.cross(self.q), -10)
        self.assertEqual(self.q.cross(self.p), 10)
        self.assertEqual(self.p.cross(Point(2, 4)), 0)
        self.assertEqual(Point(1, 0).cross(Point(0, 1)), 1)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertEqual(self.q.length(), 5)
        self.assertEqual(Point(0, 0).length(), 0)
        self.assertAlmostEqual(Point(1, 1).length(), math.sqrt(2))

    def test_hash(self):
        self.assertEqual(hash(self.p), hash(Point(1, 2)))
        points = {Point(1, 2), Point(1, 2), Point(3, -4)}
        self.assertEqual(len(points), 2)
        self.assertIn(Point(3, -4), points)


if __name__ == "__main__":
    unittest.main()
