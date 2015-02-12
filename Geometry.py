
from math import sqrt

class Point(object):
   """Class that defines Point structure in 2D Cartesian space."""
   def __init__(self, x, y):
       self._x_coordinate = x
       self._y_coordinate = y

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
    def __init__(self, point_one, point_two):
        self._first_point = point_one
        self._second_point = point_two
        self._coefficient_a = point_two.get_y() - point_one.get_y()
        self._coefficient_b = point_one.get_x() - point_two.get_x()
        self._coefficient_c = self._coefficient_a * point_one.get_x() + self._coefficient_b * point_one.get_y()

    def do_intersect(self, other):
    
        determinant = 1.0 * self._coefficient_a * other._coefficient_b - other._coefficient_a * self._coefficient_b

        if not determinant:
            return False, Point(float("inf"), float("inf"))
        else:
            intersection_x = (other._coefficient_b * self._coefficient_c - self._coefficient_b * other._coefficient_c) / determinant
            intersection_y = (other._coefficient_c * self._coefficient_a - self._coefficient_c * other._coefficient_a) / determinant
            
        return True, Point(intersection_x, intersection_y)