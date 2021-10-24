import arcade


class GameRulesView(arcade.View):
    def __init__(self):
        """Initializer; uses inheritance for arcade.View
        
        Args:
            self (GameRulesView): an instance of GameRulesView.
        """
        super().__init__()


    def on_draw(self):
        """Displays rules
        
        Args:
            self (GameRulesView): an instance of GameRulesView.
        """
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_text("Game Rules", 20, 550, arcade.color.BLACK, 34)
        # objective
        arcade.draw_text("Objective:", 20, 500, arcade.color.BLUE, 20)
        arcade.draw_text("Each player attempts to beat the dealer by getting a count as close to 21 as possible,", 20 , 470, arcade.color.BLACK, 10)
        arcade.draw_text("without going over 21.",20 , 455, arcade.color.BLACK, 10)
        # card values
        arcade.draw_text("Card Values", 20, 400,arcade.color.BLUE,20)
        arcade.draw_text("Cards 1-10 are at face value. King, Queen, and Jack count as 10. Ace counts as 11.", 20, 370,arcade.color.BLACK,10)
        # Game start
        arcade.draw_text("Gameplay", 20, 335,arcade.color.BLUE,20)
        arcade.draw_text("After each player has placed a bet. The dealer shuffles the deck and deals 2 cards face", 20, 320,arcade.color.BLACK,10)
        arcade.draw_text("up to all the players. The dealer also receives 2 card, but one is face up and the other",20,305,arcade.color.BLACK,10)
        arcade.draw_text("is face down",20,290,arcade.color.BLACK,10)

        # Game moves
        arcade.draw_text("The player can choose between 2 moves:",20,260,arcade.color.BLACK,10)
        arcade.draw_text("STAND(press the S key)- not ask for another card",20,245,arcade.color.BLACK,10)
        arcade.draw_text("Hit(press the H key) - Ask for another card in an attempt to get closer to 21",20,230,arcade.color.BLACK,10)
        
        # Win or lose
        arcade.draw_text("If the players cards add up to anything above 21 they 'BUST' and lose their bet",20,200,arcade.color.BLACK,10)
        arcade.draw_text("Once all players are at a BUST or STAND, the dealer reveals his cards.",20,185,arcade.color.BLACK,10)
        arcade.draw_text("If the players cards are closer to 21 the player collects the bet",20,170,arcade.color.BLACK,10)
        arcade.draw_text("If the dealer is closer to 21 the player loses the bet.",20,155,arcade.color.BLACK,10)



