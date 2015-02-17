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
        self.line_one = LineSegment((0,0), (250,0))
        self.line_two = LineSegment((0,0), (0,250))
        self.line_three = LineSegment((250,0), (250,250))
        self.line_four = LineSegment((0,250), (250,250))

    
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

        
    def test_point_in_segment(self):
        self.assertTrue(self.line_one._in_segment(Point(60,0)))
        self.assertFalse(self.line_one._in_segment(Point(60,5)))
        self.assertTrue(self.line_two._in_segment(Point(0,121)))
        self.assertFalse(self.line_two._in_segment(Point(0,300)))
        self.assertTrue(self.line_four._in_segment(Point(160,250)))
        self.assertFalse(self.line_four._in_segment(Point(60,247)))

if __name__ == '__main__':
  unittest.main()
#suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
#unittest.TextTestRunner(verbosity=2).run(suite)
