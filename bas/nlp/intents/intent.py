from abc import ABC, abstractmethod


class Intent(ABC):
    def __init__(self, intent, game_master):
        self.__intent = intent
        self.game_master = game_master

    @property
    def intent(self):
        return self.__intent

    @abstractmethod
    def execute(self, message=None, nlp_data=None):
        pass
