import arcade


class Game(arcade.Window):

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
