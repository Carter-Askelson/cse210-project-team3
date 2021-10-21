import arcade
from game.game import Game


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Blackjack"


def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_game()
    arcade.run()

if __name__ == "__main__":
    main()