import arcade



class Card(arcade.Sprite):
    """ Card sprite """

    def __init__(self, suit, value, scale=1):
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
        """ Turn card face-down """
        self.texture = arcade.load_texture(self.face_down_image)
        self.is_face_up = False

    def face_up(self):
        """ Turn card face-up """
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True


    def __repr__(self):
            x = self.value + " of " \
             + self.suit
            return x