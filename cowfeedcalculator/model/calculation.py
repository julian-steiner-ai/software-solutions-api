"""
Class for Calculuation.
"""

from cowfeedcalculator.model.feed_type import FeedType

class Calculation:
    """
    Base class for a calculation.
    """
    def __init__(self, name):
        self.name = name
        self.feed_types = []

    def add_feed_type(self, feed_type : FeedType):
        """
        Add new Feed Type to list.
        """
        self.feed_types.append(feed_type)

    def to_json(self):
        """
        Convert Object to JSON.
        """
        return {
            'name': self.name,
            'feed_types': [feed_type.to_json() for feed_type in self.feed_types]
        }
