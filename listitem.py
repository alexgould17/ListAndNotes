"""A module containing the ListItem class.
"""

import enum


class ListItem:
    """A superclass for all the potential items that can be added to a List.

    Class variables:
    status - enumerated list of possible completion statuses of an item.
    recurrence - enumerated list of the possible intervals of recurrence.
    status_icons: dict mapping each potential status to a single character that can be displayed in the box in string conversion to indicate the item's status.
    """
    status = enum.Enum('status', ['complete', 'incomplete', 'partial', 'progress'
                       , 'backburner', 'abandoned'])
    recurrence = enum.Enum('recurrence', ['daily', 'weekly', 'monthly', 'yearly'])
    status_icons = {status.complete: 'x', status.incomplete: ' ', status.partial: 'o'
                    , status. progress: '>', status.backburner: '<', status.abandoned: '_'}

    def __init__(self, status=None, is_time_sensitive=False, recurrence=None, recurrence_interval=-1
                 , scheduled_time=-1, text=''):
        """Constructor. status initialized to incomplete if not given."""
        if status:
            self.status = status
        else:
            self.status = self.status.incomplete

        # Initialize other variables
        self.is_time_sensitive = is_time_sensitive
        self.recurrence = recurrence
        self.recurrence_interval = recurrence_interval
        self.scheduled_time = scheduled_time
        self.text = text

    def __str__(self):
        """String conversion. For now, in command line mode, we include a box indicating the status."""
        return '[' + self.status_icons[self.status] + '] ' + self.text

    def __le__(self, other):
        """Compares two items by their scheduled_time attribute & returns the less than or equal to comparison.
        Returns None if other is not a ListItem.
        """
        if isinstance(other, ListItem):
            return self.scheduled_time <= other.scheduled_time

    def __lt__(self, other):
        """Compares two items by their scheduled_time attribute & returns the less than comparison.
        Returns None if other is not a ListItem.
        """
        if isinstance(other, ListItem):
            return self.scheduled_time < other.scheduled_time

    def __ge__(self, other):
        """Compares two items by their scheduled_time attribute & returns the greater than or equal to comparison.
        Returns None if other is not a ListItem.
        """
        if isinstance(other, ListItem):
            return self.scheduled_time >= other.scheduled_time

    def __gt__(self, other):
        """Compares two items by their scheduled_time attribute & returns the greater than comparison.
        Returns None if other is not a ListItem.
        """
        if isinstance(other, ListItem):
            return self.scheduled_time > other.scheduled_time

    def __eq__(self, other):
        """Compares two items by their scheduled_time attribute & returns the equal to comparison.
        Returns None if other is not a ListItem.
        """
        if isinstance(other, ListItem):
            return self.scheduled_time == other.scheduled_time

    def __ne__(self, other):
        """Compares two items by their scheduled_time attribute & returns the not equal to comparison.
        Returns None if other is not a ListItem.
        """
        if isinstance(other, ListItem):
            return self.scheduled_time != other.scheduled_time
