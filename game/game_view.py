import arcade

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.cards_list = None
        self.sound = arcade.Sound(":resources:sounds/laser1.wav")
        self.pan = 0
        self.volume = 1

    def setup(self):
        self.cards_list = arcade.SpriteList()
    
    def play(self):
        """ Play """
        self.sound.play(pan=self.pan, volume=self.volume)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_text("Blackjack game will be here.", 65, 425, arcade.color.BLACK, 16)
        ##self.cards_list.draw()

    
    def draw_card(self):
        card_seven = arcade.Sprite(":resources:images/cards/cardHearts7.png", 1)
        card_seven.center_x = 0
        card_seven.center_y = 0
        self.cards_list.append(card_seven)
