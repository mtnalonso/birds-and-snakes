from pprint import pprint

from bas.nlp.intents.add_game_people import AddGamePeople
from bas.nlp.intents.create_game import CreateGame
from bas.nlp.intents.list_games import ListGames
import bas.nlp.keywords as keywords
from bas.nlp.nlp import NLPFactory
import bas.config as config


class MessageHandler:
    def __init__(self, game_master):
        self.game_master = game_master
        self.nlp_service = NLPFactory.create(config.nlp_session_id)

    def process(self, message):
        preprocessed_message = self.__get_preprocessed_message(message)
        nlp_data = self.nlp_service.get_message_data(preprocessed_message)
        intent = self.__get_intent(nlp_data)
        response = intent.execute(message, nlp_data)
        return response

    def __get_preprocessed_message(self, message):
        preprocessed_message = message.message
        if '@' in preprocessed_message:
            preprocessed_message = self.__replace_usernames(message)
        if '#' in preprocessed_message:
            preprocessed_message = self.__replace_game_key(message)
        return preprocessed_message

    def __replace_usernames(self, message):
        split_message = message.split(' ')
        parsed_split_message = [x if x[0] != '@'
                                else keywords.PLAYER for x in split_message]
        return ' '.join(parsed_split_message)

    def __replace_game_key(self, message):
        # TODO: replace game key with game key keyword
        # keywords.GAME_KEY
        return message

    def __get_intent(self, nlp_data):
        intent_tag = self.__get_intent_tag(nlp_data)
        intent = None

        if intent_tag == 'create-game':
            intent = CreateGame
        if intent_tag == 'list-user-games':
            intent = ListGames

        if intent is not None:
            return intent(self.game_master)
        else:
            logger.error('Intent not recognized', nlp_data)
            raise NotImplementedError

    def __get_intent_tag(self, nlp_data):
        result = nlp_data['result']
        intent_tag = result['action']
        if intent_tag == '':
            intent_tag = result['metadata']['intentName']
        return intent_tag
