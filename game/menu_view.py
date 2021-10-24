import arcade


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.window_width = 800

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("Welcome to Blackjack", self.window_width / 2, self.window_width / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Press 'E' to enter into a game of Blackjack", self.window_width / 2,
                         self.window_width / 2 - 75,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press 'L' to learn the rules of Blackjack", self.window_width / 2.12,
                         self.window_width / 2 - 120,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
