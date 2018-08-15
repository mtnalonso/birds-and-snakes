from bas.db.database import db
from bas.db.model.character import Character
from bas.db.model.character_class import CharacterClass
from bas.db.model.race import Race
from bas.nlp.intents.intent import Intent
import bas.db.model.game_state as game_state


class CreateCharacter(Intent):
    def __init__(self, game_master):
        super().__init__('create-character', game_master)
        self.game = self.game_master.game

    def execute(self, message, nlp_data):
        user = message.user

        if self.is_action_complete(nlp_data):
            character = self.create_character(user, nlp_data)
            response = '[+] Created character "{}" ({})\n'.format(
                    character.name,
                    character.character_class
            )
            response += self.check_other_players_if_in_game()
        else:
            response = self.get_fulfillment(nlp_data)
        return response

    def create_character(self, user, nlp_data):
        parameters = self.get_parameters(nlp_data)

        name = self.get_name(parameters)
        race = self.get_race(parameters)
        character_class = self.get_character_class(parameters)

        character = Character(name, user=user, race=race)
        character.character_class = character_class

        user.characters.append(character)
        if user.default_character is None:
            user.default_character = character
            print('[+] Set {} as default character for {}'.format(
                character.name, user
            ))
        db.insert(character)
        return character

    def get_name(self, parameters):
        name = parameters['any']
        return name

    def get_race(self, parameters):
        race_name = parameters['race']
        race = db.find(Race, name=race_name)
        return race

    def get_character_class(self, parameters):
        character_class_name = parameters['character-class']
        character_class = db.find(CharacterClass, name=character_class_name)
        return character_class

    def check_other_players_if_in_game(self):
        if self.game is not None:
            if self.game.players_have_characters_set():
                response = 'Every player seems set\n'
                response += 'Let me know when you are ready to begin!\n'
                self.game.state = game_state.awaiting_start_confirmation()
                db.session.commit()
                return response
        return ''
