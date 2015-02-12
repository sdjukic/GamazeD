#!/usr/bin/env python3

import unittest
from Geometry import Point, LineSegment
from math import sqrt

class TestGeometry(unittest.TestCase):
  
    def setUp(self):
        self.point_one = Point(0,0)
        self.point_two = Point(1,1)
        self.point_three = Point(10,0)
        self.point_four = Point(30,20)
        self.line_one = LineSegment(Point(0,0), Point(250,0))
        self.line_two = LineSegment(Point(0,0), Point(0,250))
        self.line_three = LineSegment(Point(250,0), Point(250,250))
        self.line_four = LineSegment(Point(0,250), Point(250,250))

    def test_exceptions(self): 
        pass

    def test_point_distance(self):
        self.assertAlmostEqual(self.point_one.euclidean_distance(self.point_two), sqrt(2))
        self.assertAlmostEqual(self.point_one.euclidean_distance(self.point_three), 10)
        self.assertAlmostEqual(self.point_two.euclidean_distance(self.point_four), 34.67, places = 2) 
        self.assertAlmostEqual(self.point_two.euclidean_distance(self.point_two), 0)

    def test_line_intersection(self):
        self.assertTrue(self.line_one.do_intersect(self.line_two)[0])
        self.assertFalse(self.line_one.do_intersect(self.line_four)[0])
        self.assertFalse(self.line_two.do_intersect(self.line_three)[0])
        self.assertTrue(self.line_three.do_intersect(self.line_four)[0])


if __name__ == '__main__':
  unittest.main()
#suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
#unittest.TextTestRunner(verbosity=2).run(suite)
