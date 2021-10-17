import arcade


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
        arcade.draw_text("Welcome to Blackjack", 50, 425, arcade.color.BLACK, 34)
        arcade.draw_text("Press 'E' to enter into a game of Blackjack", 100, 325, arcade.color.BLACK, 16)
        arcade.draw_text("Press 'L' to learn the rules of Blackjack", 100, 225, arcade.color.BLACK, 16)
        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """

        if symbol == arcade.key.E:
            # Go to game window
            game_view = GameView()
            self.window.show_view(game_view)
            pass
        elif symbol == arcade.key.L:
            # Go to game rules window
            print("You pressed L")
            pass

    def update(self, delta_time):
        pass

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_text("Welcome to Blackjack", 50, 425, arcade.color.BLACK, 34)
        arcade.finish_render()
