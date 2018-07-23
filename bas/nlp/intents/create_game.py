from bas.db.database import db
from bas.db.model.game import Game
from bas.nlp.intents.intent import Intent


class CreateGame(Intent):
    def __init__(self, game_master):
        super().__init__('create-game', game_master)

    def execute(self, message, nlp_data):
        return 'CREATING NEW GAME'
        # TODO: if user has already an active game, create the game not active
        user = message.user
        game = Game()
        game.users.append(user)
        db.insert(game)
        self.game_master.active_games[game.key] = game
        return '\n[+] Created new game\n{}'.format(game)
