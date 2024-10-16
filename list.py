"""
A module containing the List class
"""

from enum import Enum
from listitem import *


class List:
    """
    A class describing the list container that hold's the program's items.

    Class variables:
    persistence - an Enum that describes the persistence of the list itself.

    Instance variables:
    display_name - user-defined name for displaying within graphical contexts.
    items - a python-native list containing all the items on this List
    """

    persistence = Enum('Persistence', ['persists', 'archived', 'deleted'])

    def __init__(self, display_name='Generic List'):
        """Constructor, takes an optional display_name argument."""
        self.display_name = display_name
        self.items = []

    def add(self, item):
        """
        Adds an item to the list if it's of the type ListItem.

        Returns:
            0 if successful
            1 if item is not a ListItem
        """
        if isinstance(item, ListItem):
            self.items.append(item)
            return 0
        else:
            return 1

    def remove(self, item):
        """
        Removes an item if it can be found.

        Returns:
            0 if successful
            1 if item isn't found
        """
        try:
            i = self.items.index(item)
            del self.items[i]
        except ValueError:
            return 1

        return 0

    def change_name(self, name):
        """
        Changes the value of display_name to name.

        Returns:
            0 if successful
            1 if name is not a string
        """
        if isinstance(name, str):
            self.display_name = name
            return 0
        else:
            return 1
