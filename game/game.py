import arcade
from .game_rules_view import GameRules
from .game_view import GameView


class Game(arcade.View):

    def __init__(self):
        super().__init__()
        self.yes = False

    def start_game(self):
        self.setup()

    def setup(self):
        self.on_draw()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_text("Welcome to Blackjack", 65, 425, arcade.color.BLACK, 34)
        arcade.draw_text("Press 'E' to enter into a game of Blackjack", 100, 325, arcade.color.BLACK, 16)
        arcade.draw_text("Press 'L' to learn the rules of Blackjack", 100, 225, arcade.color.BLACK, 16)

        arcade.finish_render()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """

        if symbol == arcade.key.E:
            # Go to game window
            print("e")
            game_view = GameView()
            self.window.show_view(game_view)

        elif symbol == arcade.key.L:
            # Go to game rules window
            print("You pressed L")
            GameRules.on_draw(self)
