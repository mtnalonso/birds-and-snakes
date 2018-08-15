from bas.db.database import db
import bas.db.model.game_state as game_state
from bas.nlp.intents.intent import Intent
import bas.manager as manager


class AddGamePeople(Intent):
    def __init__(self, game_master):
        super().__init__('add-game-people', game_master)
        self.game = game_master.game

    def execute(self, message, nlp_data):
        if self.game is None:
            return '[-] Game is not created!!'

        response = 'Users:\n'

        for username in message.tagged_usernames:
            user = manager.get_user_or_create_if_new(username)
            self.game.users.append(user)
            self.game_master.add_user(user)
            response += '{}\n'.format(user)
        db.update()

        response += 'were added to the game.\n'
        response += self.check_players_characters()
        self.update_game_state()
        return response

    def check_players_characters(self):
        response = ''
        for user in self.game.users:
            if user.default_character is None:
                response += '{} needs to create a character!\n'.format(
                    user.username
                )
        return response

    def update_game_state(self):
        if self.game.players_have_characters_set():
            self.game.state = game_state.awaiting_start_confirmation()
        else:
            self.game.state = game_state.awaiting_characters()
        return
