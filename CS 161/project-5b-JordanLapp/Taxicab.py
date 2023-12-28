# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/3/23
# Description: Created a class representing a taxicab.

class Taxicab:
    """Represents a taxicab that can move on two dimensions and tracks distance."""

    def __init__(self, x_coord, y_coord):
        """Creates a taxicab with specified x and y coordinates and odometer set to 0."""
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """Returns current x coordinate."""
        return self._x_coord

    def get_y_coord(self):
        """Returns current y coordinate."""
        return self._y_coord

    def get_odometer(self):
        """Returns total distance traveled."""
        return self._odometer

    def move_x(self, distance):
        """Moves the cab the specified distance in the x dimension."""
        self._x_coord += distance
        self._odometer += abs(distance)

    def move_y(self, distance):
        """Moves the cab the specified distance in the y dimension."""
        self._y_coord += distance
        self._odometer += abs(distance)
