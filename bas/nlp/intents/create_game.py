from bas.db.database import db
from bas.db.model.game import Game
from bas.nlp.intents.intent import Intent


class CreateGame(Intent):
    def __init__(self, game_master):
        super().__init__('create-game', game_master)

    def execute(self, message, nlp_data):
        user = message.user
        game = Game()
        game.users.append(user)
        db.insert(game)
        self.game_master.active_games[game.key] = game
        return '[+] Created new game\n{}'.format(game)
