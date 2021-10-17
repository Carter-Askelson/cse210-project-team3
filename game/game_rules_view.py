import arcade


class GameRulesView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_text("Game Rules", 65, 425, arcade.color.BLACK, 34)


