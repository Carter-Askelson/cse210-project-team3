import arcade
from game.game import Game
from game.menu_view import MenuView

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Blackjack"


def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_game()
    arcade.run()

if __name__ == "__main__":
    main()