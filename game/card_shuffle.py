import arcade
from .game_view import GameView

class CardShuffleGif(arcade.View):

    def on_show(self):
        self.gif = arcade.load_animated_gif("game\penguin\card.gif")
        self.gif.center_x = 400
        self.gif.center_y = 300
        self.time = 0
        self.game_view = GameView(self)


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.get_four_byte_color([11,15,19]))
        self.gif.draw()
        
    def on_update(self, delta_time): 
        self.gif.update_animation()
        self.time += 1
        print(self.time)
        if self.time == 900:
            return

