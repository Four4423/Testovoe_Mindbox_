import unittest
from geometry.shapes import *

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=5)
        expected_area = math.pi * 5**2
        self.assertAlmostEqual(circle.area(), expected_area)

    def test_triangle_area_heron(self):
        triangle = Triangle(a=3, b=4, c=5)
        expected_area = 6.0
        self.assertAlmostEqual(triangle.area(), expected_area)

    def test_is_right_triangle(self):
        right_triangle = Triangle(a=3, b=4, c=5)
        non_right_triangle = Triangle(a=5, b=5, c=8)
        self.assertTrue(right_triangle.is_right_triangle())
        self.assertFalse(non_right_triangle.is_right_triangle())

if __name__ == '__main__':
    unittest.main()