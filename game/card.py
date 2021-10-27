import arcade



class Card(arcade.Sprite):
    """Represents a card within the Blackjack game.

    Attributes:
        suit (int): determines the suit of the card
        value (int): card number
        face_down_image (img): image through arcade library
        is_face_up (boolean): detect if card should be face up or not
        texture (texture): arcade texture
    """

    def __init__(self, suit, value, scale=1):
        """Initializes attributes and uses inheritance for arcade.Sprite
        
        Args:
            self (Card): an instance of Card.
            suit (int): determines the suit of the card
            value (int): card number
            scale (int): size of the card
        """
        """ Card constructor """

        # Attributes for suit and value
        self.suit = suit
        self.value = value
        self.face_down_image = ":resources:images/cards/cardBack_red4.png"

        # Image to use for the sprite when face up
        self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"
        #need to make first dealer card face down
        self.is_face_up = True
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")

    def face_down(self):
        """Turns dealers first card face-down
        
        Args:
            self (Card): an instance of Card.
        """
        self.texture = arcade.load_texture(self.face_down_image)
        self.is_face_up = False

    def face_up(self):
        """Turns cards up
        
        Args:
            self (Card): an instance of Card.
        """
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True


    def __repr__(self):
        """Grabs the right card and suit
        
        Args:
            self (Card): an instance of Card.
        """
        x = self.value + " of " \
            + self.suit
        return x