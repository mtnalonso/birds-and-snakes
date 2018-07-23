from bas.nlp.intents.intent import Intent


class AddGamePeople(Intent):
    def __init__(self, game_master):
        super().__init__('add-game-people', game_master)

    def execute(self, message, nlp_data):
        raise NotImplementedError
