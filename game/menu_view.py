import arcade


class MenuView(arcade.View):
<<<<<<< HEAD
=======
    def __init__(self):
        super().__init__()
        self.window_width = 800
>>>>>>> c8cc0bb5db8e88f4650295312df0e90bed7dc8ef

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.gif = arcade.load_animated_gif("game\penguin\penguin2.gif")
        self.gif.center_x = 350
        self.gif.center_y = 350

    def on_draw(self):
        arcade.start_render()
<<<<<<< HEAD
        self.gif.draw()
        arcade.draw_text("Welcome to Blackjack", 600 / 2, 600 / 2,
=======

        arcade.draw_text("Welcome to Blackjack", self.window_width / 2, self.window_width / 2,
>>>>>>> c8cc0bb5db8e88f4650295312df0e90bed7dc8ef
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Press 'E' to enter into a game of Blackjack", self.window_width / 2,
                         self.window_width / 2 - 75,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press 'L' to learn the rules of Blackjack", self.window_width / 2.12,
                         self.window_width / 2 - 120,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
<<<<<<< HEAD

    def on_update(self, delta_time): 
        self.gif.update_animation()
=======
>>>>>>> c8cc0bb5db8e88f4650295312df0e90bed7dc8ef
