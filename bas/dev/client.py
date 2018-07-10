from threading import Thread
import requests
import json


class DevClient(Thread):
    def __init__(self, host='localhost', port=9876, username=None):
        Thread.__init__(self)
        self.is_running = False
        self.port = str(port)
        self.host = host
        self.username = username

    def start(self):
        if self.username is None:
            self.username = input('username: ')
        self.is_running = True
        super().start()

    def run(self):
        while self.is_running:
            self.get_new_message()
        return

    def stop(self):
        self.is_running = False

    def get_new_message(self):
        message = input('> ')
        if message in ['exit', ':q']:
            raise SystemExit
        url = 'http://{}:{}'.format(self.host, self.port)
        data = {'message': message, 'user': self.username}
        requests.post(url, json=data)


if __name__ == '__main__':
    DevClient().start()
