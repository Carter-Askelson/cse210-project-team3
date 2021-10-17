import arcade
from .game_rules_view import GameRulesView
from .game_view import GameView
from .menu_view import MenuView


class Game(arcade.View):

    def __init__(self):
        super().__init__()
        self.yes = False

        self.menu_view = MenuView()
        self.game_view = GameView()
        self.game_rules_view = GameRulesView()

    def start_game(self):
        self.setup()

    def setup(self):
        self.show_view(self.menu_view)
        arcade.get_window().center_window()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.E:
            # Go to game window
            print("'E' key pressed")
            self.show_view(self.game_view)

        elif symbol == arcade.key.L:
            # Go to game rules window
            print("'L' key pressed")
            self.show_view(self.game_rules_view)

