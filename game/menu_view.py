import arcade


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to Blackjack", 600 / 2, 600 / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Press 'E' to enter into a game of Blackjack", 600 / 2, 600 / 2 - 75,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press 'L' to learn the rules of Blackjack", 600 / 2, 600 / 2 - 100,
                         arcade.color.BLACK, font_size=20, anchor_x="center")


