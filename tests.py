import arcade

from game.continue_game_view import ContinueGameView
from game.game_rules_view import GameRulesView
from game.game_view import GameView
from game.menu_view import MenuView
from game.two_player_game_view import TwoPlayer_GameView
from game.two_player_continue_game_view import TwoPlayerContinueGameView
from game.game import Game
import pytest
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Blackjack"

def test_key_press():
    """Checks to see if the create_bricks() is putting its 84 bricks in the proper y positions

    Stereotype:
        Controller
​
    Attributes:
        None
    """
    testgame = Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    testgame.setup()
    testgame.on_key_press(arcade.key.E, 0)
    assert testgame.ingame == True
    assert testgame.one_player == True
    print("Hello")

test_key_press()