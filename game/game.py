<<<<<<< HEAD

=======
>>>>>>> d998714d9b6a257fffb942bd267d6057ad8b451e
import arcade


class Game(arcade.Window):
<<<<<<< HEAD
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        pass

    def on_draw(self):
        pass


    def update(self, delta_time): #update updates on it's own this is an event listener!!!
        pass
        

    def on_key_press(self, symbol: int, modifiers: int):
        pass
=======

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

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
            print("You pressed E")
            pass
        elif symbol == arcade.key.L:
            # Go to game rules window
            print("You pressed L")
            pass
>>>>>>> d998714d9b6a257fffb942bd267d6057ad8b451e
