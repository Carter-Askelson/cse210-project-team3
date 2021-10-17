import arcade

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.cards_list = None
        self.cards_list = arcade.SpriteList()
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_text("Blackjack game will be here.", 65, 425, arcade.color.BLACK, 16)
        self.cards_list.draw()
    
    def draw_card(self):
        card_seven = arcade.Sprite(":resources:images/cards/cardHearts7.png", 1)
        card_seven.center_x = 50
        card_seven.center_y = 50
        self.cards_list.append(card_seven)
