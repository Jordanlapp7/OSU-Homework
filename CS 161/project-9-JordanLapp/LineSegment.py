# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/31/23
# Description: Contains a point class with an x and y coordinate and line segment class
# that creates a line segment using two point objects.

class Point:
    """Represents a point on a coordinate plane with an x and y coordinate."""
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        """Returns the point's x coordinate."""
        return self._x_coord

    def get_y_coord(self):
        """Returns the point's y coordinate."""
        return self._y_coord

    def distance_to(self, location):
        """Returns the distance between the object the method is called on and the object passed as an argument"""
        return (((location.get_x_coord() - self._x_coord) ** 2) + ((location.get_y_coord() - self._y_coord) ** 2)) ** 0.5


class LineSegment:
    """Creates a line segment between two point objects."""
    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        """Returns endpoint 1."""
        return self._endpoint_1

    def get_endpoint_2(self):
        """Returns endpoint 2."""
        return self._endpoint_2

    def length(self):
        """Returns the length of the line segment."""
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        """Returns the slope of the line segment."""
        y_difference = self._endpoint_2.get_y_coord() - self._endpoint_1.get_y_coord()
        x_difference = self._endpoint_2.get_x_coord() - self._endpoint_1.get_x_coord()
        return y_difference / x_difference

    def is_parallel_to(self, other_line):
        """Returns true if line segments are parallel, otherwise returns false."""
        if abs(self.slope() - other_line.slope() < 1e-7):
            return True
        return False
