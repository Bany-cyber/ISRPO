import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_1(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_2(self):
        res = area(5)
        self.assertAlmostEqual(res, 25 * math.pi)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_1(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_perimeter_2(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 20 * math.pi)