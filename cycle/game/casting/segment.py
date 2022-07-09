import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Segment(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, head):
        """Create a new segment"""
        super().__init__()
        self._head = head

    def get_color(self):
        """
        Get Color of the Segment, dependent on if player is dead
        Returns:
            color of segment
        """
        if self._head.get_is_dead():
            return constants.WHITE
        else:
            return super().get_color()

    def get_head(self):
        """
        Returns the head of the segment
        Returns:
            Cycle object of the head

        """
        return self._head

