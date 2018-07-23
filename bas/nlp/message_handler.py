from pprint import pprint

from bas.nlp.intents.add_game_people import AddGamePeople
from bas.nlp.intents.create_game import CreateGame
from bas.nlp.intents.list_games import ListGames
from bas.nlp.nlp import NLPFactory
import bas.config as config


class MessageHandler:
    def __init__(self, game_master):
        self.game_master = game_master
        self.nlp_service = NLPFactory.create(config.nlp_session_id)

    def process(self, message):
        nlp_data = self.nlp_service.get_message_data(message.message)
        intent = self.__get_intent(nlp_data)
        response = intent.execute(message, nlp_data)
        return response

    def __get_intent(self, nlp_data):
        intent_tag = self.__get_intent_tag(nlp_data)
        print(intent_tag)
        if intent_tag == 'create-game':
            intent = CreateGame
        if intent_tag == 'list-user-games':
            intent = ListGames
        else:
            raise NotImplementedError
        return intent(self.game_master)

    def __get_intent_tag(self, nlp_data):
        result = nlp_data['result']
        intent_tag = result['action']
        if intent_tag == '':
            intent_tag = result['metadata']['intentName']
        return intent_tag
