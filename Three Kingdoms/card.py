class Card:
    def __init__(self, short_name):
        self.short_name = short_name

        if self.short_name == "ATT":
            self.full_name = "Attack"
            self.image_name = "attack.png"
        elif self.short_name == "DOD":
            self.full_name = "Dodge"
            self.image_name = "dodge.png"
        elif self.short_name == "PEA":
            self.full_name = "Peach"
            self.image_name = "peach.png"
        else:
            self.full_name = "Invalid"
