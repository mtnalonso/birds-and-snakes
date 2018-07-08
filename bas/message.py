
class Message:
    def __init__(self, message, user=None):
        self.__message = message
        self.__user = user

    @property
    def message(self):
        return self.__message

    @property
    def user(self):
        return self.__user

    def __str__(self):
        return '{}: {}'.format(self.user, self.message)

    @classmethod
    def from_string(cls, message):
        user, message = message.split(':', 1)
        return cls(message.lstrip(), user)
