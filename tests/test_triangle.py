import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_1(self):
        res = area(4, 5)
        self.assertEqual(res, 10)

    def test_area_2(self):
        res = area(3, 5)
        self.assertEqual(res, 7.5)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_1(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_2(self):
        res = perimeter(6, 6, 6)
        self.assertEqual(res, 11)