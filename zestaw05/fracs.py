import unittest
from math import gcd


def _check(frac):
    if len(frac) != 2:
        raise ValueError("fraction must be [numerator, denominator]")
    if frac[1] == 0:
        raise ValueError("denominator must not be zero")


def _make(num, den):
    divisor = gcd(num, den)
    num, den = num // divisor, den // divisor
    if den < 0:
        num, den = -num, -den
    return [num, den]


def add_frac(frac1, frac2):
    _check(frac1)
    _check(frac2)
    return _make(frac1[0] * frac2[1] + frac2[0] * frac1[1],
                 frac1[1] * frac2[1])


def sub_frac(frac1, frac2):
    _check(frac1)
    _check(frac2)
    return _make(frac1[0] * frac2[1] - frac2[0] * frac1[1],
                 frac1[1] * frac2[1])


def mul_frac(frac1, frac2):
    _check(frac1)
    _check(frac2)
    return _make(frac1[0] * frac2[0], frac1[1] * frac2[1])


def div_frac(frac1, frac2):
    _check(frac1)
    _check(frac2)
    if frac2[0] == 0:
        raise ZeroDivisionError("division by a zero fraction")
    return _make(frac1[0] * frac2[1], frac1[1] * frac2[0])


def is_positive(frac):
    _check(frac)
    return frac[0] * frac[1] > 0


def is_zero(frac):
    _check(frac)
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    difference = sub_frac(frac1, frac2)
    return (difference[0] > 0) - (difference[0] < 0)


def frac2float(frac):
    _check(frac)
    return frac[0] / frac[1]


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.half = [1, 2]
        self.third = [1, 3]

    def test_add_frac(self):
        self.assertEqual(add_frac(self.half, self.third), [5, 6])
        self.assertEqual(add_frac(self.half, self.half), [1, 1])
        self.assertEqual(add_frac([-1, 2], self.half), self.zero)
        self.assertEqual(add_frac([1, -2], self.half), self.zero)
        self.assertEqual(add_frac([2, 4], [3, 6]), [1, 1])
        self.assertEqual(add_frac([3, 1], [6, 2]), [6, 1])
        self.assertEqual(add_frac(self.half, self.zero), self.half)
        self.assertEqual(add_frac([0, 2], [0, 5]), self.zero)

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.half, self.third), [1, 6])
        self.assertEqual(sub_frac(self.third, self.half), [-1, 6])
        self.assertEqual(sub_frac(self.half, self.half), self.zero)
        self.assertEqual(sub_frac(self.half, [1, -2]), [1, 1])
        self.assertEqual(sub_frac(self.zero, self.half), [-1, 2])
        self.assertEqual(sub_frac([3, 4], [5, 4]), [-1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), self.half)
        self.assertEqual(mul_frac([-1, 2], [1, -2]), [1, 4])
        self.assertEqual(mul_frac([-1, 2], [1, 2]), [-1, 4])
        self.assertEqual(mul_frac(self.half, self.zero), self.zero)
        self.assertEqual(mul_frac([0, 2], [5, 7]), self.zero)
        self.assertEqual(mul_frac([3, 1], [1, 3]), [1, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac(self.half, self.third), [3, 2])
        self.assertEqual(div_frac(self.half, [-1, 3]), [-3, 2])
        self.assertEqual(div_frac([-1, 2], [-1, 3]), [3, 2])
        self.assertEqual(div_frac(self.zero, self.half), self.zero)
        self.assertEqual(div_frac([6, 2], [3, 1]), [1, 1])
        with self.assertRaises(ZeroDivisionError):
            div_frac(self.half, self.zero)
        with self.assertRaises(ZeroDivisionError):
            div_frac(self.half, [0, 5])

    def test_is_positive(self):
        self.assertTrue(is_positive(self.half))
        self.assertTrue(is_positive([-1, -2]))
        self.assertTrue(is_positive([3, 1]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))
        self.assertFalse(is_positive(self.zero))
        self.assertFalse(is_positive([0, -3]))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertTrue(is_zero([0, 2]))
        self.assertTrue(is_zero([0, -2]))
        self.assertFalse(is_zero(self.half))
        self.assertFalse(is_zero([-1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.half, self.third), 1)
        self.assertEqual(cmp_frac(self.third, self.half), -1)
        self.assertEqual(cmp_frac(self.half, [2, 4]), 0)
        self.assertEqual(cmp_frac([-1, 2], [1, -2]), 0)
        self.assertEqual(cmp_frac([-1, 2], [-1, 3]), -1)
        self.assertEqual(cmp_frac([1, -2], self.third), -1)
        self.assertEqual(cmp_frac(self.zero, [0, 7]), 0)
        self.assertEqual(cmp_frac([3, 1], [6, 2]), 0)
        self.assertEqual(cmp_frac([-1, 2], self.zero), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float(self.half), 0.5)
        self.assertEqual(frac2float([-1, 2]), -0.5)
        self.assertEqual(frac2float([1, -4]), -0.25)
        self.assertEqual(frac2float([3, 1]), 3.0)
        self.assertEqual(frac2float([0, 5]), 0.0)
        self.assertAlmostEqual(frac2float(self.third), 0.3333333333)

    def test_zero_denominator(self):
        bad = [1, 0]
        for function in (add_frac, sub_frac, mul_frac, div_frac, cmp_frac):
            with self.assertRaises(ValueError):
                function(bad, self.half)
            with self.assertRaises(ValueError):
                function(self.half, bad)
        for function in (is_positive, is_zero, frac2float):
            with self.assertRaises(ValueError):
                function(bad)
            with self.assertRaises(ValueError):
                function([0, 0])

    def test_wrong_length(self):
        with self.assertRaises(ValueError):
            add_frac([1], self.half)
        with self.assertRaises(ValueError):
            mul_frac(self.half, [1, 2, 3])

    def test_arguments_not_modified(self):
        a, b = [2, 4], [-3, -6]
        for function in (add_frac, sub_frac, mul_frac, div_frac):
            result = function(a, b)
            self.assertEqual(a, [2, 4])
            self.assertEqual(b, [-3, -6])
            self.assertIsNot(result, a)
            self.assertIsNot(result, b)

    def test_results_are_reduced(self):
        for numerator in range(-6, 7):
            for denominator in (-4, -3, -2, -1, 1, 2, 3, 4):
                result = add_frac([numerator, denominator], self.zero)
                self.assertGreater(result[1], 0)
                self.assertEqual(gcd(result[0], result[1]),
                                 1 if result[0] else result[1])
                self.assertEqual(result[0] * denominator,
                                 numerator * result[1])


if __name__ == '__main__':
    unittest.main()
