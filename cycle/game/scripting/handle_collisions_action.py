import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the food, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            score = cast.get_first_actor("scores")

            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            if self._is_game_over == False:
                score.add_points(1)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("cycles")
        player2 = cast.get_second_actor("cycles")
        player1head = player1.get_segments()[0]
        player2head = player2.get_segments()[0]
        player1segments = player1.get_segments()[1:]
        player2segments = player2.get_segments()[1:]

        # player 1 segment check
        for segment in player1segments:
            if player1head.get_position().equals(segment.get_position()) or player2head.get_position().equals(
                    segment.get_position()):
                player2.set_is_dead()
                self._is_game_over = True

        # player 2 segment check
        for segment in player2segments:
            if player1head.get_position().equals(segment.get_position()) or player2head.get_position().equals(
                    segment.get_position()):
                player2.set_is_dead()
                self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            # food.set_color(constants.WHITE)
