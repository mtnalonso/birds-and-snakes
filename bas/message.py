from bas.db.database import db
from bas.db.model.user import User
import bas.manager as manager
import bas.nlp.keywords as keywords


class Message:
    def __init__(self, message, username=None):
        self.__message = message
        self.__username = username
        self.__user = manager.get_user_or_create_if_new(self.username)
        self.tagged_usernames = []
        self.__load_tagged_usernames()

    @property
    def message(self):
        return self.__message

    @property
    def username(self):
        return self.__username

    @property
    def user(self):
        return self.__user

    def __str__(self):
        return '{}: {}'.format(self.username, self.message)

    @classmethod
    def from_string(cls, message):
        username, message = message.split(':', 1)
        return cls(message.lstrip(), username)

    def __load_tagged_usernames(self):
        message_words = self.message.split(' ')
        for word in message_words:
            if word[0] == '@':
                self.tagged_usernames.append(word[1:])
        return

    def get_preprocessed_message(self):
        preprocessed_message = self.message
        if '@' in preprocessed_message:
            preprocessed_message = self.__replace_usernames()
        return preprocessed_message

    def __replace_usernames(self):
        split_message = self.message.split(' ')
        parsed_split_message = [x if x[0] != '@'
                                else keywords.PLAYER for x in split_message]
        return ' '.join(parsed_split_message)
