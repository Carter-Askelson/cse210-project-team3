import arcade


class ContinueGameView(arcade.View):
    """Responsible for letting the use continue to play another game or quit the game all together

    Attributes:
        window_width (int): defines the width of the view.
        victory (bool): used to know if the player won the current game or not.
        defeat(bool): used to know if the player lost the current game or not.
        game_over(bool): used to know if the player ran out of chips in the current game.
    """

    def __init__(self, victory=False, defeat=False, game_over=False):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (ContinueGameView): an instance of ContinueGameView.
        """
        super().__init__()
        self.window_width = 800
        self.victory = victory
        self.defeat = defeat
        self.game_over = game_over

    def set_victory(self, victory):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (ContinueGameView): an instance of ContinueGameView.
            victory (Boolean): stores if the player won or not
        """
        self.victory = victory

    def set_defeat(self, defeat):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (ContinueGameView): an instance of ContinueGameView.
            defeat (Boolean): stores if the player lost or not
        """
        self.defeat = defeat

    def set_game_over(self, game_over):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (ContinueGameView): an instance of ContinueGameView.
            game_over (Boolean): stores if the player has chips left or not
        """
        self.game_over = game_over

    def on_show(self):
        """sets background color
        
        Args:
            self (ContinueGameView): an instance of ContinueGameView.
        """
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """Displays message depending on the above booleans
        
        Args:
            self (ContinueGameView): an instance of ContinueGameView.
        """
        arcade.start_render()

        if self.victory:
            arcade.draw_text("You Won", self.window_width / 2, self.window_width / 2, arcade.color.BLUE, 64,
                             anchor_x="center")
            arcade.draw_text("Would you like to play again? [Y/N]", self.window_width / 2, self.window_width / 2 - 75,
                             arcade.color.BLUE, 24, anchor_x="center")
        elif self.defeat:
            arcade.draw_text("You Lost", self.window_width / 2, self.window_width / 2, arcade.color.RED, 64,
                             anchor_x="center")
            arcade.draw_text("Would you like to play again? [Y/N]", self.window_width / 2, self.window_width / 2 - 75,
                             arcade.color.RED, 24, anchor_x="center")
        if self.game_over:
            arcade.draw_text("All out of Chips", self.window_width / 2, self.window_width / 2, arcade.color.BLACK, 64,
                             anchor_x="center")
            arcade.draw_text("Press [Q] to quit game, (in shame)", self.window_width / 2, self.window_width / 2 - 75,
                             arcade.color.BLACK, 24, anchor_x="center")