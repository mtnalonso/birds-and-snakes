from datetime import datetime
from bas.level import Level
from bas.player import Player


class Game:
    def __init__(self, key):
        self.__key = key
        self.players = {}
        self.levels = []
        self.last_message_date = None
        self.levels.append(Level('start'))

    @property
    def key(self):
        return self.__key

    def add_player(self, player):
        self.players[player.username] = player

    def action(self, message):
        self.last_action_date = datetime.now()
        return '{} {}'.format(self.last_action_date, message)

    def print_levels(self):
        screen_levels = '\n{}\n'.format(self.key)
        for level in self.levels:
            if level.is_active():
                screen_levels += '{}\n'.format(level.name)
                screen_levels += level.print_map()
        return screen_levels

