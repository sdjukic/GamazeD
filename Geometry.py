from math import sqrt

class Point(object):
     """Class that defines Point structure in 2D Cartesian space."""
     def __init__(self, *args):
         self._x_coordinate = args[0]
         self._y_coordinate = args[1]

     def get_x(self):
         return self._x_coordinate

     def get_y(self):
         return self._y_coordinate

     def set_x(self, new_x):
         self._x_coordinate = new_x

     def set_y(self, new_y):
         self._y_coordinate = new_y

     def euclidean_distance(self, other):
         return sqrt((self._x_coordinate - other.get_x())**2 + (self._y_coordinate - other.get_y())**2)


class LineSegment(object):
    """Class that defines Line Segment in 2D Cartesian space."""
    def __init__(self, *points):
        self.end_points = []
        self.end_points.append(Point(points[0][0], points[0][1]))
        self.end_points.append(Point(points[1][0], points[1][1]))
        self.segment_length = self.end_points[0].euclidean_distance(self.end_points[1])
        
        self._coefficient_a = self.end_points[1].get_y() - self.end_points[0].get_y()
        self._coefficient_b = self.end_points[0].get_x() - self.end_points[1].get_x()
        self._coefficient_c = self._coefficient_a * self.end_points[0].get_x() + self._coefficient_b * self.end_points[0].get_y()

    def do_intersect(self, other):
    
        determinant = 1.0 * self._coefficient_a * other._coefficient_b - other._coefficient_a * self._coefficient_b

        if not determinant:
            return False, Point(float("inf"), float("inf"))
        else:
            intersection_x = (other._coefficient_b * self._coefficient_c - self._coefficient_b * other._coefficient_c) / determinant
            intersection_y = (other._coefficient_c * self._coefficient_a - self._coefficient_c * other._coefficient_a) / determinant
            
        return True, Point(intersection_x, intersection_y)

    
    def _in_segment(self, point):
        """Function that checks whether point is in the segment."""
        distance_from_endpoints = 0
        for p in self.end_points:
            distance_from_endpoints += point.euclidean_distance(p)
            
        return abs(distance_from_endpoints - self.segment_length) < 0.05