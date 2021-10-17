import arcade
from .game_rules_view import GameRulesView
from .game_view import GameView
from .menu_view import MenuView


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.menu_view = MenuView()
        self.game_view = GameView()
        self.game_rules_view = GameRulesView()
        self.audio_name = arcade.sound.load_sound(":resources:sounds/laser1.wav")
        self.audio_name_two = arcade.sound.load_sound(":resources:sounds/hurt2.wav")


    def start_game(self):
        self.setup()

    def setup(self):
        self.show_view(self.menu_view)
        arcade.get_window().center_window()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.E:
            # Go to game window
            print("'E' key pressed")
            arcade.sound.play_sound(self.audio_name)
            self.show_view(self.game_view)

        elif symbol == arcade.key.L:
            # Go to game rules window
            print("'L' key pressed")
            arcade.sound.play_sound(self.audio_name_two)
            self.show_view(self.game_rules_view)

