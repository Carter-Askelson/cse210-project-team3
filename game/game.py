
import arcade


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        pass

    def on_draw(self):
        pass


    def update(self, delta_time): #update updates on it's own this is an event listener!!!
        pass
        

    def on_key_press(self, symbol: int, modifiers: int):
        pass
