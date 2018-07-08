from bas.character import Character


class Player(Character):
    def __init__(self, username, character_name):
        Character.__init__(self, 50)
        self.username = username
        self.character_name = character_name

