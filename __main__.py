import arcade
from game.game import Game

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Blackjack"


def main():
    window = Game()
    window.start_game()
    arcade.run()

if __name__ == "__main__":
    main()