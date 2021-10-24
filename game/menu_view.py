import arcade


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.window_width = 800

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.gif = arcade.load_animated_gif("game\penguin\penguin2.gif")
        self.gif.center_x = 350
        self.gif.center_y = 350

    def on_draw(self):
        arcade.start_render()
        self.gif.draw()
        arcade.draw_text("Welcome to Blackjack", 600 / 2, 600 / 2,

        arcade.draw_text("Welcome to Blackjack", self.window_width / 2, self.window_width / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center"))
        arcade.draw_text("Press 'E' to enter into a game of Blackjack", self.window_width / 2,
                         self.window_width / 2 - 75,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press 'L' to learn the rules of Blackjack", self.window_width / 2.12,
                         self.window_width / 2 - 120,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_update(self, delta_time):
        self.gif.update_animation()
