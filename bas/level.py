

class Level:
    def __init__(self, name):
        self.__name = name
        self.players = {}
        self.default_x = 3
        self.default_y = 3
        self.map = [
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
        ]

    @property
    def name(self):
        return self.__name

    def add_player(self, player, coords=None):
        if coords is not None:
            player.x, player.y = coords
        else:
            player.x = self.default_x
            player.y = self.default_y
        self.players[player.username] = player

    def print_map(self):
        screen_map = '\n'.join(''.join(pos for pos in row) for row in self.map)
        screen_map += '\n'
        return screen_map

    def is_active(self):
        return len(self.map) > 0
