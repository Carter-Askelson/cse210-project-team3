import arcade
import arcade.gui
from .card import Card
import random
from .continue_game_view import ContinueGameView
import sys
from pathlib import Path

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
chips = 1000
placed_bet = False


class GameView(arcade.View):

    def __init__(self, continue_game_view, game_window):
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
        self.player_hand = []
        self.dealer_hand = []
        self.player_value = 0
        self.dealer_value = 0
        self.player_ace_count = 0
        self.dealer_ace_count = 0
        self.player_almost_bust = 0
        self.dealer_almost_bust = 0
        self.final_bet = 0
        self.blackjack = False
        self.victory = False
        self.defeat = False
        self.game_over = False
        self.setup_newgame()
        self.continue_game_view = continue_game_view
        self.game_window = game_window
        self.bet = 100
        
        self.gif = arcade.load_animated_gif(Path(__file__).parent / "penguin" / "card.gif")
        self.gif.center_x = 400
        self.gif.center_y = 300
        self.time = 0
        
        

    def setup_newgame(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (GameView): an instance of GameView.

        """
        global chips
        self.bet = 100
        if chips < self.bet: 
            self.game_over = True
        chips -= self.bet
        

        self.cards_list = arcade.SpriteList()

        #resets on newgame
        self.top_card_int = 0 ## this had to be moved here to make it so that you are not drawing over the 52 card limit
        self.player_hand = []
        self.dealer_hand = []
        self.player_value = 0
        self.dealer_value = 0
        self.player_ace_count = 0
        self.dealer_ace_count = 0
        self.player_almost_bust = 0
        self.dealer_almost_bust = 0
        self.blackjack = False
        self.victory = False
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
            
        #Current way to add cards to player and dealer hands since using .pop() on self.cards_list deletes the card itself even in the other hands
        
        #self.dealer_hand.append(self.top_card_int)
        self.hit("dealer")
        self.dealer_hand[0].face_down()
        #first_card = self.dealer_hand[0]
        #first_card.face_down()
        #self.dealer_hand[0].face_down()
        self.hit("player")
        self.player_hand[0].face_down()
        self.hit("dealer")
        self.dealer_hand[1].face_down()
        self.hit("player")
        self.player_hand[1].face_down()
        self.update_card_positions()
        
    def calculate_value(self, hand):
        """Calculates the value of player and dealer hand. Ends the game at or over 21 points
        
        Args:
            self (GameView): an instance of GameView.
            hand (String): keeps track of player and dealer
        """
        global FACE_CARDS
        #could refactor the 2 hand possiblities into methods of a Dealer and Player Class
        if hand == "player":
            if self.player_hand[-1].value in FACE_CARDS:
                self.player_value += 10
            elif self.player_hand[-1].value == "A":
                self.player_value += 11
                self.player_ace_count += 1
            else:
                self.player_value += int(self.player_hand[-1].value)

            if self.player_value > 21:
                if self.player_ace_count > self.player_almost_bust:
                    #To prevent a Bust, your Ace became a one
                    self.player_value -= 10
                    self.player_almost_bust += 1
                else:
                    self.player_lose()
            elif self.player_value == 21:
                self.blackjack = True
                self.endgame()

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
                        self.player_win()
                elif self.dealer_value == 21:
                    self.player_lose()

        

    def hit(self, hand):
        """Draws a card for the player's hand and the dealers hand
        
        Args:
            self (GameView): an instance of GameView.
            hand (String): keeps track of player and dealer
        """
        if hand == "player":
            self.player_hand.append(self.cards_list[self.top_card_int])
            self.calculate_value("player")
        elif hand == "dealer":
            self.dealer_hand.append(self.cards_list[self.top_card_int])
            self.calculate_value("dealer")
        self.top_card_int += 1
        self.update_card_positions()


    def double_down(self):
        """Doubles the bet and draws a card for the player
        
        Args:
            self (GameView): an instance of GameView.
        """
        global chips
        chips -= self.bet
        self.bet = self.bet * 2
        self.hit("player")
        self.endgame()

    def stand(self):
        """Ends the game when the player has draw as many cards as they want
        
        Args:
            self (GameView): an instance of GameView.
        """
        self.endgame()

    def player_win(self):
        """If the player wins give them chips
        
        Args:
            self (GameView): an instance of GameView.
        """
        global chips
        global placed_bet

        chips = (self.final_bet*2 + chips)
        self.victory = True
        placed_bet = False


    def player_lose(self):
        """if the player loses set self.defeat to true
        
        Args:
            self (GameView): an instance of GameView.
        """
        global chips
        chips = chips - self.final_bet
        self.defeat = True
        placed_bet = False

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
                self.player_win()
        #House always wins Ties
        elif self.dealer_value == 21:
            self.player_lose()

        while self.dealer_value < 17:
                self.hit("dealer")

        if (self.player_value - self.dealer_value) > 0:
           self.player_win()
        else:
            self.player_lose()
        
    

        
    
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
            arcade.draw_text("Blackjack", 65, 550, arcade.color.BLACK, 16)
            arcade.draw_text(f"Chips: {int(chips)}", 500, 80, arcade.color.BLACK, 16)
            arcade.draw_text("[H] = Hit    [D] = Double Down    [S] = Stand    [Q] = Quit Game", 65, 525, arcade.color.BLACK, 16)
            arcade.draw_text("Dealer's Hand", 80, 450, arcade.color.BLACK, 16)
            arcade.draw_text("Player's Hand", 80, 250, arcade.color.BLACK, 16)
            arcade.draw_text(f"Current Bet: {self.bet}", 500, 50, arcade.color.BLACK,16 )

            if placed_bet == True:
                arcade.draw_text(f"Value: {self.dealer_value}", 280, 450, arcade.color.BLACK, 16)
                arcade.draw_text(f"Value: {self.player_value}", 280, 250, arcade.color.BLACK, 16)
            
            self.manager = arcade.gui.UIManager()
            self.manager.enable()
            self.v_box = arcade.gui.UIBoxLayout()

# Create the buttons
            increase_bet = arcade.gui.UIFlatButton(text="Increase Bet", width=200)
            self.v_box.add(increase_bet.with_space_around(bottom=20))

            decrease_bet = arcade.gui.UIFlatButton(text="Decrease Bet", width=200)
            self.v_box.add(decrease_bet.with_space_around(bottom=20))
            
            place_bet = arcade.gui.UIFlatButton(text="Place Bet", width=200)
            self.v_box.add(place_bet.with_space_around(bottom=20))

# functions for buttons
            increase_bet.on_click = self.on_increase_bet
            decrease_bet.on_click = self.on_decrease_bet
            place_bet.on_click = self.on_place_bet

        # Create a widget to hold the v_box widget, that will center the buttons
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    anchor_x="center_x",
                    anchor_y="center_y",
                    align_x= 200,
                    align_y= 100,
                    child=self.v_box)
        )

            self.manager.draw()

            if self.blackjack:
                arcade.draw_text("Blackjack!", 480, 250, arcade.color.BLACK, 16)
            if self.game_over:
                self.continue_game_view.set_game_over(self.game_over)
                self.game_window.show_view(self.continue_game_view)
            elif self.victory:
                self.continue_game_view.set_victory(self.victory)
                self.game_window.show_view(self.continue_game_view)
            elif self.defeat:
                self.continue_game_view.set_defeat(self.defeat)
                self.game_window.show_view(self.continue_game_view)
            

        
            for i in self.dealer_hand:
                i.draw()
            for j in self.player_hand:
                j.draw()


    def on_decrease_bet(self, event):
        global chips
        if self.bet <= 50:
            self.bet = self.bet
        elif self.bet > 50:
            self.bet = self.bet - 50  
            chips = chips + 50 
    def on_increase_bet(self, event):
        global chips
        if self.bet < 1000:
            self.bet = self.bet + 50
            chips = chips - 50
        elif self.bet >= 1000:
            self.bet = self.bet

    def on_place_bet (self,event):
        global placed_bet
        placed_bet = True
        arcade.draw_text(f"Value: {self.dealer_value}", 280, 450, arcade.color.BLACK, 16)
        arcade.draw_text(f"Value: {self.player_value}", 280, 250, arcade.color.BLACK, 16)
            
        self.final_bet = self.bet
        self.dealer_hand[1].face_up()
        self.player_hand[0].face_up()
        self.player_hand[1].face_up()
            
    
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
        x_position = 100
        for i in self.dealer_hand:
            i.position = (x_position, dealer_y)
            x_position += 100
        x_position = 100
        for j in self.player_hand:
            j.position = (x_position, player_y)
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
        global placed_bet

        if symbol == arcade.key.H and not self.game_over and placed_bet == True:
            # Hit
            arcade.sound.play_sound(audio_name_three)
            self.hit("player")

        elif symbol == arcade.key.D and not self.game_over and placed_bet == True:
            # Double Down
            arcade.sound.play_sound(audio_name_four)
            self.double_down()

        elif symbol == arcade.key.S and not self.game_over and placed_bet == True:
            # Stand
            arcade.sound.play_sound(audio_name_five)
            self.stand()