import arcade
from .card import Card
import random

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



class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        #self.cards_list = None
        self.cards_list = []
        self.top_card_int = 0
        self.player_hand = []
        self.dealer_hand = []
        #self.drawn_cards = []
        self.setup_newgame()
        
        

    def setup_newgame(self):
        self.cards_list = arcade.SpriteList()
        
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
        self.dealer_hand.append(self.cards_list[self.top_card_int])
        self.update_top_card()

        #self.player_hand.append(self.top_card_int)
        self.player_hand.append(self.cards_list[self.top_card_int])
        self.update_top_card()

        #self.dealer_hand.append(self.top_card_int)
        self.dealer_hand.append(self.cards_list[self.top_card_int])
        self.update_top_card()

        #self.player_hand.append(self.top_card_int)
        self.player_hand.append(self.cards_list[self.top_card_int])
        self.update_top_card()


        #test code for checking hand values
        # x = 0
        # y = 0
        # for i in self.dealer_hand:
        #     x += int(i.value)
        # for j in self.player_hand:
        #     y += int(j.value)
        # print(f"Dealer hand is {str(x)}")
        # print(f"Player hand is {str(y)}")


        self.update_card_positions()
        

        



        
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_text("Blackjack game will be here.", 65, 525, arcade.color.BLACK, 16)
        arcade.draw_text("Dealer's Hand", 80, 450, arcade.color.BLACK, 16)
        arcade.draw_text("Player's Hand", 80, 250, arcade.color.BLACK, 16)
        for i in self.dealer_hand:
            i.draw()
        for j in self.player_hand:
            j.draw()
        


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


    
    def update_top_card(self):
        self.top_card_int += 1

        


