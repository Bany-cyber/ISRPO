import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_2(self):
        res = area(3, 4)
        self.assertEqual(res, 12)

    def test_perimeter_1(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_perimeter_2(self):
        res = perimeter(0, 5)
        self.assertEqual(res, 10)