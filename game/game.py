import arcade

from .continue_game_view import ContinueGameView
from .game_rules_view import GameRulesView
from .game_view import GameView
from .menu_view import MenuView


class Game(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        menu_view (MenuView): an instance of MenuView
        continue_game_view (ContinueGameView): an instance of ContinueGameView
        game_view (GameView): an instance of GameView
        game_rules_view (GameRulesView): an instance of GameRulesView
        audio_name (sound): a sound from the arcade library
        audio_name_two (sound): a sound from the arcade library
        self.audio_name_three (sound): a sound from the arcade library
        self.audio_name_four (sound): a sound from the arcade library
        self.audio_name_five (sound): a sound from the arcade library
        self.ingame (boolean): indicates wether the user is playing the game or not
    """
    def __init__(self, width, height, title):
        """Initializes attributes
        
        Args:
            self (Game): an instance of Game.
            widthe (int): width of the screen
            height(int): height of the screen
            title (string): the title of the game
        """
        super().__init__(width, height, title)

        self.menu_view = MenuView()
        self.continue_game_view = ContinueGameView()
        self.game_view = GameView(self.continue_game_view, self)
        self.game_rules_view = GameRulesView()
        self.audio_name = arcade.sound.load_sound(":resources:sounds/laser1.wav")
        self.audio_name_two = arcade.sound.load_sound(":resources:sounds/hurt2.wav")
        
        self.audio_name_three = arcade.sound.load_sound(":resources:sounds/rockHit2.wav")
        self.audio_name_four = arcade.sound.load_sound(":resources:sounds/coin3.wav")
        self.audio_name_five = arcade.sound.load_sound(":resources:sounds/coin4.wav")
        self.ingame = False


    def start_game(self):
        """Starts the game
        
        Args:
            self (Game): an instance of Game.
        """
        self.setup()

    def setup(self):
        """dispalys the main menu
        
        Args:
            self (Game): an instance of Game.
        """
        self.show_view(self.menu_view)
        arcade.get_window().center_window()

    def on_key_press(self, symbol: int, modifiers: int):
        """Controls the sequence of play.
        
        Args:
            self (Game): an instance of Game.
            symbol (int): this takes user input
            modifiers (int): this takes user input
        """
        if symbol == arcade.key.E:
            # Go to game window
            arcade.sound.play_sound(self.audio_name)
            self.show_view(self.game_view)
            self.ingame = True


        elif symbol == arcade.key.L:
            # Go to game rules window
            arcade.sound.play_sound(self.audio_name_two)
            self.show_view(self.game_rules_view)

        elif symbol == arcade.key.B:
            self.hide_view()
            self.show_view(self.menu_view)

        elif symbol == arcade.key.N and (self.game_view.victory or self.game_view.defeat):
            # Quit
            self.close()

        elif symbol == arcade.key.Y and (self.game_view.victory or self.game_view.defeat):
            # Restart
            arcade.sound.play_sound(self.audio_name)
            self.hide_view()
            self.continue_game_view.victory = False
            self.show_view(self.game_view)
            self.game_view.setup_newgame()

        elif symbol == arcade.key.Q:
            self.close()


            

            


