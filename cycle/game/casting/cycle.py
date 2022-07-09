import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.segment import Segment


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, start_x, start_y, color_of_cycle=constants.GREEN):
        """
        Constructs the new cycle actor
        Args:
            start_x: starting x position
            start_y: starting y position
        """
        super().__init__()
        self._default_cycle_color = color_of_cycle
        self._segments = []
        self._prepare_body(start_x, start_y)

    def get_segments(self):
        """
        returns a list of segments

        Returns:
            list of segments that are part of this cycle
        """
        return self._segments

    def set_is_dead(self):
        """
        Marks this cycle as dead

        Returns:

        """
        self._is_dead = True


    def get_color(self):
        """
        Overrides parent get_color to track death and its color

        Returns:
            Color of the cycle

        """
        if super()._is_dead:
            return constants.WHITE
        else:
            return super().get_color()

    def move_next(self):
        """
        Move the cycle and all segments

        Returns:
            nothing

        """
        # move all segments
        for segment in self._segments:
            segment.move_next()
        self.grow_tail(1)
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """
            Returns the head object
        Returns:
            Actor that is the head
        """

        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """
        Grows tail by number of segments
        Args:
            number_of_segments: segments to create
        Returns:

        """
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Segment(self)
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            if self._is_dead:
                segment.set_color(constants.WHITE)
            else:
                segment.set_color(self._default_cycle_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """
            Change direction of movement
        Args:
            velocity: the direction to change

        Returns:

        """
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, start_x = 0, start_y = 0):
        """
        Does the initial creation of the cycle
        Args:
            start_x: starting X position
            start_y: Starting y position

        Returns:
            Nothing

        """
        x = start_x
        y = start_y

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 1)
            text = "8" if i == 0 else "#"
            color = self._default_cycle_color
            
            segment = Segment(self)
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)