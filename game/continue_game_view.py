import arcade


class ContinueGameView(arcade.View):

    def __init__(self, victory=False, defeat=False, game_over=False):
        super().__init__()
        self.victory = victory
        self.defeat = defeat
        self.game_over = game_over

    def set_victory(self, victory):
        self.victory = victory

    def set_defeat(self, defeat):
        self.defeat = defeat

    def set_game_over(self, game_over):
        self.game_over = game_over

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()

        if self.victory:
            arcade.draw_text("You Won", 65, 525, arcade.color.BLUE, 64)
            arcade.draw_text("Would you like to play again? [Y/N]", 65, 425, arcade.color.BLUE, 24)
        elif self.defeat:
            arcade.draw_text("You Lost", 65, 525, arcade.color.RED, 64)
            arcade.draw_text("Would you like to play again? [Y/N]", 65, 425, arcade.color.RED, 24)
        if self.game_over:
            arcade.draw_text("All out of Chips", 65, 525, arcade.color.BLACK, 64)
            arcade.draw_text("Press [Q] to quit game, (in shame)", 65, 425, arcade.color.BLACK, 24)
