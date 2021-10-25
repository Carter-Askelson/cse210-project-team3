import arcade


class TwoPlayerContinueGameView(arcade.View):
    """Responsible for letting the use continue to play another game or quit the game all together

    Attributes:
        window_width (int): defines the width of the view.
        victory (bool): used to know if the player won the current game or not.
        defeat(bool): used to know if the player lost the current game or not.
        game_over(bool): used to know if the player ran out of chips in the current game.
    """

    def __init__(self, victory1=False, victory2=False, both_victory=False, defeat=False, game_over1=False, game_over2=False):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (ContinueGameView): an instance of ContinueGameView.
        """
        super().__init__()
        self.window_width = 800
        self.victory1 = victory1
        self.victory2 = victory2
        self.both_victory = both_victory
        self.defeat = defeat
        self.game_over1 = game_over1
        self.game_over2 = game_over2

    def set_victory1(self, victory1):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (TwoPlayerContinueGameView): an instance of TwoPlayerContinueGameView.
            victory (Boolean): stores if the player won or not
        """
        self.victory1 = victory1

    def set_victory2(self, victory2):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (TwoPlayerContinueGameView): an instance of TwoPlayerContinueGameView.
            victory (Boolean): stores if the player won or not
        """
        self.victory2 = victory2

    def set_both_victory(self, both_victory):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (TwoPlayerContinueGameView): an instance of TwoPlayerContinueGameView.
            victory (Boolean): stores if the player won or not
        """
        self.both_victory = both_victory

    def set_defeat(self, defeat):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (TwoPlayerContinueGameView): an instance of TwoPlayerContinueGameView.
            defeat (Boolean): stores if the player lost or not
        """
        self.defeat = defeat

    def set_game_over1(self, game_over1):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (TwoPlayerContinueGameView): an instance of TwoPlayerContinueGameView.
            game_over (Boolean): stores if the player has chips left or not
        """
        self.game_over1 = game_over1

    def set_game_over2(self, game_over2):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (TwoPlayerContinueGameView): an instance of TwoPlayerContinueGameView.
            game_over (Boolean): stores if the player has chips left or not
        """
        self.game_over2 = game_over2

    def on_show(self):
        """sets background color
        
        Args:
            self (TwoPlayerContinueGameView): an instance of TwoPlayerContinueGameView.
        """
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """Displays message depending on the above booleans
        
        Args:
            self (TwoPlayerContinueGameView): an instance of TwoPlayerContinueGameView.
        """
        arcade.start_render()

        if self.victory1:
            arcade.draw_text("Player 1 Won", self.window_width / 2, self.window_width / 2, arcade.color.BLUE, 64,
                             anchor_x="center")
            arcade.draw_text("Would you like to play again? [Y/N]", self.window_width / 2, self.window_width / 2 - 75,
                             arcade.color.BLUE, 24, anchor_x="center")
        elif self.victory2:
            arcade.draw_text("Player 2 Won", self.window_width / 2, self.window_width / 2, arcade.color.BLUE, 64,
                             anchor_x="center")
            arcade.draw_text("Would you like to play again? [Y/N]", self.window_width / 2, self.window_width / 2 - 75,
                             arcade.color.BLUE, 24, anchor_x="center")
        elif self.both_victory:
            arcade.draw_text("Both Players Won", self.window_width / 2, self.window_width / 2, arcade.color.BLUE, 64,
                             anchor_x="center")
            arcade.draw_text("Would you like to play again? [Y/N]", self.window_width / 2, self.window_width / 2 - 75,
                             arcade.color.BLUE, 24, anchor_x="center")
        elif self.defeat:
            arcade.draw_text("You Both Lost", self.window_width / 2, self.window_width / 2, arcade.color.RED, 64,
                             anchor_x="center")
            arcade.draw_text("Would you like to play again? [Y/N]", self.window_width / 2, self.window_width / 2 - 75,
                             arcade.color.RED, 24, anchor_x="center")
        if self.game_over1:
            arcade.draw_text("Player 1 ran out of Chips", self.window_width / 2, self.window_width / 2, arcade.color.BLACK, 64,
                             anchor_x="center")
            arcade.draw_text("Press [Q] to quit game, (Player 2 Wins!)", self.window_width / 2, self.window_width / 2 - 75,
                             arcade.color.BLACK, 24, anchor_x="center")
        elif self.game_over2:
            arcade.draw_text("Player 2 ran out of Chips", self.window_width / 2, self.window_width / 2, arcade.color.BLACK, 64,
                             anchor_x="center")
            arcade.draw_text("Press [Q] to quit game, (Player 1 Wins!)", self.window_width / 2, self.window_width / 2 - 75,
                             arcade.color.BLACK, 24, anchor_x="center")