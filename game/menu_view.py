from pathlib import Path

import arcade
from pathlib import Path

class MenuView(arcade.View):
    """Responsible for the main menu of the game. User interacts with this menu
    to learn about Blackjack or play a game of Blackjack.
    
    attributes:
        gif (gif): loads a gif via arcade
        gif.center_x and gif.center_y (int): positions gif

    """
    def on_show(self):
        """displays gif to the user and sets a background color
        
        Args:
            self (MenuView): an instance of MenuView.
        """
        arcade.set_background_color(arcade.color.AMAZON)
        self.gif = arcade.load_animated_gif(Path(__file__).parent / "penguin" / "penguin2.gif")
        self.gif.center_x = 350
        self.gif.center_y = 350

    def on_draw(self):
        """displays gif to the user and sets a background color
        
        Args:
            self (MenuView): an instance of MenuView.
        """
        arcade.start_render()
        self.gif.draw()
        arcade.draw_text("Welcome to Blackjack", 600 / 2, 600 / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Press 'E' to enter into a game of Blackjack", 600 / 2, 600 / 2 - 75,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press 'T' to enter a into 2 player game of Blackjack", 746 / 2, 600 / 2 - 100,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press 'L' to learn the rules of Blackjack", 640 / 2, 600 / 2 - 125,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_update(self, delta_time): 
        """Updates the gif if self.time is less than or equal to 900
        
        Args:
            self (MenuView): an instance of MenuView.
            delta_time (time): calls this function every 1/60th of a second
        """
        self.gif.update_animation()
