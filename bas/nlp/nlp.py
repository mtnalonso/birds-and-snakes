from abc import ABC, abstractmethod

import bas.config as config


class NLPResponseError(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return '<NLPResponseError({!r})>'.format(self.message)

    def __str__(self):
        return self.message


class NLP(ABC):
    def __init__(self, session_id):
        self.language = config.language
        self.session_id = session_id

        def validate_response(response):
            status_code = int(response['status']['code'])
            if status_code != 200:
                raise NLPResponseError('status code {}'.format(status_code))

        @abstractmethod
        def get_message_data(self, message):
            pass

        @abstractmethod
        def build_request(self, message):
            pass


class NLPFactory:
    from bas.nlp.dialogflow import DialogflowV1

    classes = {
        'dialogflow-v1': DialogflowV1,
    }

    @staticmethod
    def create(session_id):
        nlp_service = NLPFactory.classes.get(config.nlp_service)
        return nlp_service(session_id)
