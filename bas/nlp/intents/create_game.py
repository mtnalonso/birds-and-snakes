from bas.db.database import db
from bas.db.model.game import Game
from bas.db.model.story import Story
from bas.nlp.intents.intent import Intent
import bas.db.model.game_state as game_state


class CreateGame(Intent):
    def __init__(self, game_master):
        super().__init__('create-game', game_master)

    def execute(self, message, nlp_data):
        if self.game is None:
            response = self.create_new_game(message)
        elif self.game.state == game_state.awaiting_characters():
            response = self.start_game_if_ready()
        elif self.game.state == game_state.awaiting_start_confirmation():
            response = self.start_game()
        return response

    def create_new_game(self, message):
        user = message.user
        game = Game()
        game.users.append(user)
        game.state = game_state.awaiting_characters()
        game.story = db.find(Story, name='Test Story')
        db.insert(game)
        self.game_master.game = game
        self.game = game

        response = '[+] Created new game\n{}\n'.format(game)
        response += '\n- Who else wants to join the game?\n'
        response += '(tag user / nobody)'
        return response

    def start_game_if_ready(self):
        if self.game.players_have_characters_set():
            self.game.state = game_state.awaiting_start_confirmation()
            db.session.commit()
            return '\n- Let me know when you are ready to begin'
        return '[-] Every user must have a character created!'

    def start_game(self):
        if self.game.state != game_state.started():
            self.game.state = game_state.started()
            # TODO: add level to game
            db.session.commit()

            response = '[+] STARTING THE ADVENTURE\n'
            response += self.game.story.introduction
            return response
        return '[-] The adventure has already started long ago...'
