""""
A superclass representing any item that can potentially be added to our list.
"""

import enum


class ListItem:
    # Class variables
    # status: enumerated list of possible completion statuses of an item.
    status = enum.Enum('status', ['complete', 'incomplete', 'partial', 'progress'
                       , 'backburner', 'abandoned'])

    # recurrence: enumerated list of the possible intervals of recurrence.
    recurrence = enum.Enum('recurrence', ['daily', 'weekly', 'monthly', 'yearly'])

    # status_icons: dict mapping each potential status to a single character that can be displayed
    # in the box in string conversion to indicate the item's status
    status_icons = {status.complete: 'x', status.incomplete: ' ', status.partial: 'o'
                    , status. progress: '>', status.backburner: '<', status.abandoned: '_'}

    # Constructor. status initialized to incomplete if not given.
    def __init__(self, status=None, is_time_sensitive=False, recurrence=None, recurrence_interval=-1
                 , scheduled_time=-1, text=''):
        # Initialize status to incomplete if not given, otherwise to given value.
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

    # String conversion. For now, in command line mode, we include a box indicating the status.
    def __str__(self):
        return '[' + self.status_icons[self.status] + '] ' + self.text

    # All 6 comparison operators: compare strictly based on scheduled_time. The later of the two
    # is considered "greater". Checks to make sure other is also a ListItem instance.
    def __le__(self, other):
        if isinstance(other, ListItem):
            return self.scheduled_time <= other.scheduled_time

    def __lt__(self, other):
        if isinstance(other, ListItem):
            return self.scheduled_time < other.scheduled_time

    def __ge__(self, other):
        if isinstance(other, ListItem):
            return self.scheduled_time >= other.scheduled_time

    def __gt__(self, other):
        if isinstance(other, ListItem):
            return self.scheduled_time > other.scheduled_time

    def __eq__(self, other):
        if isinstance(other, ListItem):
            return self.scheduled_time == other.scheduled_time

    def __ne__(self, other):
        if isinstance(other, ListItem):
            return self.scheduled_time != other.scheduled_time
