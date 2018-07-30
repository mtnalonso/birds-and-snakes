from bas.db.database import db
from bas.db.model.character import Character
from bas.db.model.character_class import CharacterClass
from bas.db.model.race import Race
from bas.nlp.intents.intent import Intent


class CreateCharacter(Intent):
    def __init__(self, game_master):
        super().__init__('create-character', game_master)

    def execute(self, message, nlp_data):
        user = message.user

        if self.is_action_complete(nlp_data):
            character = self.create_character(user, nlp_data)
            return '[+] Created character "{}" ({})'.format(
                    character.name,
                    character.character_class
            )
        else:
            # TODO: add context to master
            return self.get_fulfillment(nlp_data)

    def create_character(self, user, nlp_data):
        parameters = self.get_parameters(nlp_data)

        name = self.get_name(parameters)
        race = self.get_race(parameters)
        character_class = self.get_character_class(parameters)

        character = Character(name, user=user, race=race)
        character.character_class = character_class

        user.characters.append(character)
        db.insert(character)
        return character

    def get_name(self, parameters):
        name = parameters['any']
        return name

    def get_race(self, parameters):
        race_name = parameters['race']
        race = db.first(Race, name=race_name)
        return race

    def get_character_class(self, parameters):
        character_class_name = parameters['character-class']
        character_class = db.first(CharacterClass, name=character_class_name)
        return character_class
