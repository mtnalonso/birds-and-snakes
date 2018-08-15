from threading import Thread

from bas.game_master import GameMaster


class SystemMaster(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.game_masters = []
        self.game_masters_by_user = {}

    def start(self):
        self.is_running = True
        super().start()

    def run(self):
        while self.is_running:
            self.update()
        return

    def update(self):
        if not self.queue.empty():
            self.redirect_message_to_game_master()
        return

    def stop(self):
        for game_master in self.game_masters:
            game_master.join()
        self.is_running = False

    def redirect_message_to_game_master(self):
        message = self.queue.get()
        user = message.user
        if user.id not in self.game_masters_by_user:
            game_master = GameMaster(self)
            game_master.start()
            self.game_masters.append(game_master)
            self.game_masters_by_user[user.id] = game_master
        game_master = self.game_masters_by_user[user.id]
        game_master.new_message(message)

    def add_user(self, game_master, user):
        self.game_masters_by_user[user.id] = game_master
