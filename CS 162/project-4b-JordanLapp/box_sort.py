# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/16/2023
# Description: Contains a Box class with dimensions and volume method, and insertion sort that sorts boxes by volume.

class Box:
    """Creates a box with a length, width, and height. Contains method to return volume."""
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """Returns box length."""
        return self._length

    def get_width(self):
        """Returns box width."""
        return self._width

    def get_height(self):
        """Returns box height."""
        return self._height

    def volume(self):
        """Returns box volume"""
        return self._length * self._width * self._height


def box_sort(box_list):
    """Insertion sorts a list of boxes by volume"""
    for index in range(1, len(box_list)):
        value = box_list[index]
        pos = index - 1
        while pos >= 0 and box_list[pos].volume() < value.volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = value
    return
