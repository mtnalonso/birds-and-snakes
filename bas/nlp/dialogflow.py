import json

import apiai

import bas.config as config
from bas.nlp.nlp import NLP


class DialogflowV1(NLP):
    def __init__(self, session_id):
        super().__init__(session_id)
        self.key = config.nlp_service_key
        self.api = apiai.ApiAI(self.key)

    def get_message_data(self, message):
        request = self.build_request(message)
        response = request.getresponse()
        return json.loads(response.read().decode('utf-8'))

    def build_request(self, message):
        request = self.api.text_request()
        request.query = message.get_preprocessed_message()
        request.lang = self.language
        request.session_id = '{}.{}'.format(self.session_id,
                                            message.user.id)
        return request
