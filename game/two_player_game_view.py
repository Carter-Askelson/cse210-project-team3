import arcade
from .card import Card
import random
from .two_player_continue_game_view import TwoPlayerContinueGameView
import sys

# Constants for sizing


CARD_SCALE = 0.6

# How big are the cards?
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

# How big is the mat we'll place the card on?
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)

# How much space do we leave as a gap between the mats?
# Done as a percent of the mat size.
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

# The Y of the bottom row (2 piles)
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The X of where to start putting things on the left side
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

# Card constants
CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]
FACE_CARDS = ["J", "Q", "K"]






#maybe bust sound gameover4.wav
#maybe win sound upgrade2.wav
chips1 = 500
chips2 = 500


class TwoPlayer_GameView(arcade.View):

    def __init__(self, TwoPlayerContinueGameView, game_window):
        """Initializes class attributes
        
        Args:
            self (GameView): an instance of GameView.
            continue_game_view (ContinueGameView): an instance of ContinueGameView
            game_window (Game): an instance of Game

        """
        super().__init__()
        #self.cards_list = None
        self.cards_list = []
        self.top_card_int = 0
        self.player1_hand = []
        self.player2_hand = []
        self.dealer_hand = []
        self.player1_value = 0
        self.player2_value = 0
        self.dealer_value = 0
        self.player1_ace_count = 0
        self.player2_ace_count = 0
        self.dealer_ace_count = 0
        self.player1_almost_bust = 0
        self.player2_almost_bust = 0
        self.dealer_almost_bust = 0
        self.player1_bust = False
        self.player2_bust = False
        self.turn1 = False
        self.turn2 = False
        self.skip1 = False
        self.skip2 = False
        self.blackjack = False
        self.victory1 = False
        self.victory2 = False
        self.both_victory = False
        self.defeat = False
        self.game_over1 = False
        self.game_over2 = False
        self.setup_newgame()
        self.two_player_continue_game_view = TwoPlayerContinueGameView
        self.game_window = game_window
        
        self.gif = arcade.load_animated_gif("game\penguin\card.gif")
        self.gif.center_x = 400
        self.gif.center_y = 300
        self.time = 0
        
        

    def setup_newgame(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (GameView): an instance of GameView.

        """
        global chips1
        global chips2
        if chips1 < 100:
            self.game_over1 = True
        elif chips1 < 100:
            self.game_over2 = True
        chips1 -= 100
        self.bet1 = 100
        chips2 -= 100
        self.bet2 = 100
        

        self.cards_list = arcade.SpriteList()

        #resets on newgame
        self.top_card_int = 0 ## this had to be moved here to make it so that you are not drawing over the 52 card limit
        self.player1_hand = []
        self.player2_hand = []
        self.dealer_hand = []
        self.player1_value = 0
        self.player2_value = 0
        self.dealer_value = 0
        self.player1_ace_count = 0
        self.player2_ace_count = 0
        self.dealer_ace_count = 0
        self.player1_almost_bust = 0
        self.player2_almost_bust = 0
        self.dealer_almost_bust = 0
        self.player1_bust = False
        self.player2_bust = False
        self.turn1 = False
        self.turn2 = False
        self.skip1 = False
        self.skip2 = False
        self.blackjack1 = False
        self.blackjack2 = False
        self.victory1 = False
        self.victory2 = False
        self.both_victory = False
        self.defeat = False
        
        #creates deck
        for card_suit in CARD_SUITS:
            for card_value in CARD_VALUES:
                card = Card(card_suit, card_value, CARD_SCALE)
                self.cards_list.append(card)
        #shuffles deck
        for pos1 in range(len(self.cards_list)):
            pos2 = random.randrange(len(self.cards_list))
            self.cards_list.swap(pos1, pos2)
            
        
        self.hit("dealer")
        self.dealer_hand[0].face_down()
        self.hit("player1")
        self.hit("player2")
        self.hit("dealer")
        self.hit("player1")
        self.hit("player2")
        self.update_card_positions()
        if self.player1_value != 21:
            self.turn1 = True
        elif self.player2_value != 21:
            self.turn2 = True
        else:
            self.endgame()
        
    def calculate_value(self, hand):
        """Calculates the value of player and dealer hand. Ends the game at or over 21 points
        
        Args:
            self (GameView): an instance of GameView.
            hand (String): keeps track of player and dealer
        """
        global FACE_CARDS
        #could refactor the 2 hand possiblities into methods of a Dealer and Player Class
        if hand == "player1":
            if self.player1_hand[-1].value in FACE_CARDS:
                self.player1_value += 10
            elif self.player1_hand[-1].value == "A":
                self.player1_value += 11
                self.player1_ace_count += 1
            else:
                self.player1_value += int(self.player1_hand[-1].value)

            if self.player1_value > 21:
                if self.player1_ace_count > self.player1_almost_bust:
                    #To prevent a Bust, your Ace became a one
                    self.player1_value -= 10
                    self.player1_almost_bust += 1
                else:
                    self.player1_bust = True
                    self.player_lose(1)
            if self.player1_value == 21:
                self.blackjack1 = True
                self.stand("player1")

        elif hand == "player2":
            if self.player2_hand[-1].value in FACE_CARDS:
                self.player2_value += 10
            elif self.player2_hand[-1].value == "A":
                self.player2_value += 11
                self.player2_ace_count += 1
            else:
                self.player2_value += int(self.player2_hand[-1].value)

            if self.player2_value > 21:
                if self.player2_ace_count > self.player2_almost_bust:
                    #To prevent a Bust, your Ace became a one
                    self.player2_value -= 10
                    self.player2_almost_bust += 1
                else:
                    self.player2_bust = True
                    self.player_lose(2)
                
            if self.player2_value == 21:
                self.blackjack2 = True
                self.stand("player2")

        elif hand == "dealer":
            if len(self.dealer_hand) > 1:
                if self.dealer_hand[-1].value in FACE_CARDS:
                    self.dealer_value += 10
                elif self.dealer_hand[-1].value == "A":
                    self.dealer_value += 11
                    self.dealer_ace_count += 1
                else:
                    self.dealer_value += int(self.dealer_hand[-1].value)

                if self.dealer_value > 21:
                    if self.dealer_ace_count > self.dealer_almost_bust:
                        #To prevent a Bust, the Dealer's Ace became a one
                        self.dealer_value -= 10
                        self.dealer_almost_bust += 1
                    else:
                        if self.player1_bust:
                            self.player2_win()
                        elif self.player2_bust:
                            self.player1_win()
                        else:
                            self.players_win()
                elif self.dealer_value == 21:
                    self.player_lose(0)

        

    def hit(self, hand):
        """Draws a card for the player's hand and the dealers hand
        
        Args:
            self (GameView): an instance of GameView.
            hand (String): keeps track of player and dealer
        """
        if hand == "player1":
            self.player1_hand.append(self.cards_list[self.top_card_int])
            self.calculate_value("player1")
            self.switch_turn()
        elif hand == "player2":
            self.player2_hand.append(self.cards_list[self.top_card_int])
            self.calculate_value("player2")
            self.switch_turn()
        elif hand == "dealer":
            self.dealer_hand.append(self.cards_list[self.top_card_int])
            self.calculate_value("dealer")
        self.top_card_int += 1
        self.update_card_positions()


    def double_down(self, player):
        """Doubles the bet and draws a card for the player, also double checks that the other player has the next turn
        
        Args:
            self (GameView): an instance of GameView.
        """
        if player == "player1":
            global chips1
            chips1 -= 100
            self.bet1 += 100
            self.skip1 = True
            self.hit("player1")
            self.stand("player1")
            self.turn1 = False
            self.turn2 = True
            if self.skip2:
                self.endgame()
            
        elif player == "player2":
            global chips2
            chips2 -= 100
            self.bet2 += 100
            self.skip2 = True
            self.hit("player2")
            self.stand("player2")
            self.turn1 = True
            self.turn2 = False
            if self.skip1:
                self.endgame()
            

    def stand(self, player):
        """Ends the game when the player has draw as many cards as they want
        
        Args:
            self (GameView): an instance of GameView.
        """
        if player == "player1":
            self.skip1 = True
            self.switch_turn()
            if self.skip2:
                self.endgame()
        elif player == "player2":
            self.skip2 = True
            self.switch_turn()
            if self.skip1:
                self.endgame()

    def switch_turn(self):
        """Makes is so the proper player has the next move
        
        Args:
            self (GameView): an instance of GameView.
        """
        if self.turn1:
            if self.skip2:
                pass
            elif self.player1_bust == False:
                self.turn1 = False
                self.turn2 = True
            else:
                self.endgame()
        elif self.turn2:
            if self.skip1:
                pass
            elif self.player2_bust == False:
                self.turn1 = True
                self.turn2 = False
            else:
                self.endgame()


    def player1_win(self):
        """If the player wins give them chips
        
        Args:
            self (GameView): an instance of GameView.
        """
        global chips1
        if self.blackjack1:
            chips1 += (self.bet1 * 2.5)
        else:
            chips1 += (self.bet1 * 2)
        self.victory1 = True

    def player2_win(self):
        """If the player wins give them chips
        
        Args:
            self (GameView): an instance of GameView.
        """
        global chips2
        if self.blackjack2:
            chips2 += (self.bet2 * 2.5)
        else:
            chips2 += (self.bet2 * 2)
        self.victory2 = True

    def players_win(self):
        """If the player wins give them chips
        
        Args:
            self (GameView): an instance of GameView.
        """
        global chips1
        global chips2
        if self.blackjack1:
            chips1 += (self.bet1 * 2.5)
        else:
            chips1 += (self.bet1 * 2)
        

        if self.blackjack2:
            chips2 += (self.bet2 * 2.5)
        else:
            chips2 += (self.bet2 * 2)
        self.both_victory = True



    def player_lose(self, player):
        """if the player loses set self.defeat to true
        
        Args:
            self (GameView): an instance of GameView.
        """

        if player == 1:
            self.skip1 = True
        elif player == 2:
            self.skip2 = True
        if (self.skip1 and self.skip2) or player == 0:
            self.defeat = True
        

    def endgame(self):
        """Ends the game - is called when the player chooses to 'stand'
        
        Args:
            self (GameView): an instance of GameView.
        """
        #reveals the dealer's first card then the dealer hits until the dealer's hand's value is above 16
        self.dealer_hand[0].face_up()
        if self.dealer_hand[0].value in FACE_CARDS:
            self.dealer_value += 10
        elif self.dealer_hand[0].value == "A":
            self.dealer_value += 11
            self.dealer_ace_count += 1
        else:
            self.dealer_value += int(self.dealer_hand[0].value)

        if self.dealer_value > 21:
            if self.dealer_ace_count > self.dealer_almost_bust:
                #To prevent a Bust, the Dealer's Ace became a one
                self.dealer_value -= 10
                self.dealer_almost_bust += 1
            else:
                self.players_win()
        #House always wins Ties
        elif self.dealer_value == 21:
            self.player_lose(0)

        while self.dealer_value < 17:
                self.hit("dealer")

        if (self.player1_value - self.dealer_value) > 0 and (self.player2_value - self.dealer_value) > 0 and self.player1_bust == False and self.player2_bust == False:
           self.players_win()
        elif (self.player1_value - self.dealer_value) > 0 and self.player1_bust == False:
           self.player1_win()
        elif (self.player2_value - self.dealer_value) > 0 and self.player2_bust == False:
           self.player2_win()
        else:
            self.player_lose(0)
        
    

        
    
    def on_draw(self):
        """draws text, gif, and victory & loss screens.
        
        Args:
            self (GameView): an instance of GameView.
        """
        arcade.start_render()
        arcade.set_background_color(arcade.get_four_byte_color([11,15,19]))
        if self.time < 900:
            self.gif.draw()
        if self.time >= 900:
            global chips
            arcade.set_background_color(arcade.color.AMAZON)
            arcade.draw_text("Blackjack", 25, 550, arcade.color.BLACK, 16)
            arcade.draw_text(f"Player 1's Chips: {int(chips1)}", 310, 550, arcade.color.BLACK, 16)
            arcade.draw_text(f"Player 2's Chips: {int(chips2)}", 560, 550, arcade.color.BLACK, 16)
            arcade.draw_text("[H] = Hit    [D] = Double Down    [S] = Stand    [Q] = Quit Game", 65, 525, arcade.color.BLACK, 16)
            arcade.draw_text("Dealer's Hand", 80, 450, arcade.color.BLACK, 16)
            arcade.draw_text("Player 1's Hand", 80, 250, arcade.color.BLACK, 16)
            arcade.draw_text("Player 2's Hand", 80, 50, arcade.color.BLACK, 16)
            arcade.draw_text(f"Value: {self.dealer_value}", 280, 450, arcade.color.BLACK, 16)
            arcade.draw_text(f"Value: {self.player1_value}", 280, 250, arcade.color.BLACK, 16)
            arcade.draw_text(f"Value: {self.player2_value}", 280, 50, arcade.color.BLACK, 16)

            if self.turn1:
                arcade.draw_text("Player 1 Turn", 145, 550, arcade.color.BLACK, 16)
            elif self.turn2 == True:
                arcade.draw_text("Player 2 Turn", 145, 550, arcade.color.BLACK, 16)
            if self.blackjack1:
                arcade.draw_text("Blackjack!", 480, 250, arcade.color.BLACK, 16)
            if self.blackjack2:
                arcade.draw_text("Blackjack!", 480, 50, arcade.color.BLACK, 16)
            elif self.both_victory:
                self.two_player_continue_game_view.set_both_victory(self.both_victory)
                self.game_window.show_view(self.two_player_continue_game_view)
            elif self.victory1:
                self.two_player_continue_game_view.set_victory1(self.victory1)
                self.game_window.show_view(self.two_player_continue_game_view)
            elif self.victory2:
                self.two_player_continue_game_view.set_victory2(self.victory2)
                self.game_window.show_view(self.two_player_continue_game_view)
            elif self.defeat:
                self.two_player_continue_game_view.set_defeat(self.defeat)
                self.game_window.show_view(self.two_player_continue_game_view)
            if self.game_over1:
                self.two_player_continue_game_view.set_game_over(self.game_over1)
                self.game_window.show_view(self.two_player_continue_game_view)
            elif self.game_over2:
                self.two_player_continue_game_view.set_game_over(self.game_over2)
                self.game_window.show_view(self.two_player_continue_game_view)

        
            for i in self.dealer_hand:
                i.draw()
            for j in self.player1_hand:
                j.draw()
            for k in self.player2_hand:
                k.draw()
            
    
    def on_update(self, delta_time): 
        """Updates the gif if self.time is less than or equal to 900
        
        Args:
            self (GameView): an instance of GameView.
            delta_time (time): calls this function every 1/60th of a second
        """
        self.time += 1
        if self.time <= 900:
            self.gif.update_animation()


    def update_card_positions(self):
        """Puts cards in the correct location on the screen
        
        Args:
            self (GameView): an instance of GameView.
            hand (String): keeps track of player and dealer
        """
        dealer_y = 350
        player_y = 150
        player_z = -50
        x_position = 100
        for i in self.dealer_hand:
            i.position = (x_position, dealer_y)
            x_position += 100
        x_position = 100
        for j in self.player1_hand:
            j.position = (x_position, player_y)
            x_position += 100
        x_position = 100
        for k in self.player2_hand:
            k.position = (x_position, player_z)
            x_position += 100




    def on_key_press(self, symbol: int, modifiers: int):
        """Controls the sequence of play.
        
        Args:
            self (GameView): an instance of GameView.
            symbol (int): this takes user input
            modifiers (int): this takes user input
        """
        audio_name = arcade.sound.load_sound(":resources:sounds/laser1.wav")
        audio_name_three = arcade.sound.load_sound(":resources:sounds/rockHit2.wav")
        audio_name_four = arcade.sound.load_sound(":resources:sounds/coin3.wav")
        audio_name_five = arcade.sound.load_sound(":resources:sounds/coin4.wav")

        if symbol == arcade.key.H and not self.game_over1 and not self.game_over2:
            # Hit
            arcade.sound.play_sound(audio_name_three)
            if self.turn1:
                self.hit("player1")
            elif self.turn2:
                self.hit("player2")

        elif symbol == arcade.key.D and not self.game_over1 and not self.game_over2:
            # Double Down
            arcade.sound.play_sound(audio_name_four)
            if self.turn1:
                self.double_down("player1")
            elif self.turn2:
                self.double_down("player2")

        elif symbol == arcade.key.S and not self.game_over1 and not self.game_over2:
            # Stand
            arcade.sound.play_sound(audio_name_five)
            if self.turn1:
                self.stand("player1")
            elif self.turn2:
                self.stand("player2")