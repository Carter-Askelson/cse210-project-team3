import arcade
from game.game import Game
from game.menu_view import MenuView

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Blackjack"


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.get_window().center_window()
    arcade.run()

if __name__ == "__main__":
    main()