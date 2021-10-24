import arcade
from .card import Card
import random
from .continue_game_view import ContinueGameView
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
chips = 1000


class GameView(arcade.View):

    def __init__(self, continue_game_view, game_window):
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
        self.blackjack = False
        self.victory = False
        self.defeat = False
        self.game_over = False
        self.setup_newgame()
        self.continue_game_view = continue_game_view
        self.game_window = game_window
        self.gif = arcade.load_animated_gif("game\penguin\card.gif")
        self.gif.center_x = 400
        self.gif.center_y = 300
        self.time = 0

    def setup_newgame(self):
        global chips
        if chips < 100:
            self.game_over = True
        chips -= 100
        self.bet = 100


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
        self.hit("dealer")
        self.hit("player")

    


        self.update_card_positions()
        
    def calculate_value(self, hand):
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
        if hand == "player":
            self.player_hand.append(self.cards_list[self.top_card_int])
            self.calculate_value("player")
        elif hand == "dealer":
            self.dealer_hand.append(self.cards_list[self.top_card_int])
            self.calculate_value("dealer")
        self.top_card_int += 1
        self.update_card_positions()


    def double_down(self):
        global chips
        chips -= 100
        self.bet += 100
        self.hit("player")
        self.endgame()

    def stand(self):
        self.endgame()

    def player_win(self):
        global chips
        if self.blackjack:
            chips += (self.bet * 2.5)
        else:
            chips += (self.bet * 2)
        self.victory = True

    def player_lose(self):
        self.defeat = True

    def endgame(self):
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
        global chips
        arcade.start_render()
        arcade.set_background_color(arcade.get_four_byte_color([11,15,19]))
        if self.time < 900:
            self.gif.draw()
        if self.time >= 900:
            arcade.set_background_color(arcade.color.AMAZON)
            arcade.draw_text("Blackjack", 65, 550, arcade.color.BLACK, 16)
            arcade.draw_text(f"Chips: {int(chips)}", 265, 550, arcade.color.BLACK, 16)
            arcade.draw_text("[H] = Hit    [D] = Double Down    [S] = Stand    [Q] = Quit Game", 65, 525, arcade.color.BLACK, 16)
            arcade.draw_text("Dealer's Hand", 80, 450, arcade.color.BLACK, 16)
            arcade.draw_text("Player's Hand", 80, 250, arcade.color.BLACK, 16)
            arcade.draw_text(f"Value: {self.dealer_value}", 280, 450, arcade.color.BLACK, 16)
            arcade.draw_text(f"Value: {self.player_value}", 280, 250, arcade.color.BLACK, 16)

        if self.blackjack:
            arcade.draw_text("Blackjack!", 480, 250, arcade.color.BLACK, 16)
        if self.victory:
            self.continue_game_view.set_victory(self.victory)
            self.game_window.show_view(self.continue_game_view)
        elif self.defeat:
            self.continue_game_view.set_defeat(self.defeat)
            self.game_window.show_view(self.continue_game_view)
        if self.game_over:
            self.continue_game_view.set_game_over(self.game_over)
            self.game_window.show_view(self.continue_game_view)


            for i in self.dealer_hand:
                i.draw()
            for j in self.player_hand:
                j.draw()


    def on_update(self, delta_time):
        self.time += 1
        if self.time <= 900:
            self.gif.update_animation()


    def update_card_positions(self):
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
        audio_name = arcade.sound.load_sound(":resources:sounds/laser1.wav")
        audio_name_three = arcade.sound.load_sound(":resources:sounds/rockHit2.wav")
        audio_name_four = arcade.sound.load_sound(":resources:sounds/coin3.wav")
        audio_name_five = arcade.sound.load_sound(":resources:sounds/coin4.wav")

        if symbol == arcade.key.H and not self.game_over:
            # Hit
            arcade.sound.play_sound(audio_name_three)
            self.hit("player")

        elif symbol == arcade.key.D and not self.game_over:
            # Double Down
            arcade.sound.play_sound(audio_name_four)
            self.double_down()

        elif symbol == arcade.key.S and not self.game_over:
            # Stand
            arcade.sound.play_sound(audio_name_five)
            self.stand()


        


