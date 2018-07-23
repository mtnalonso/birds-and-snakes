from bas.nlp.intents.intent import Intent


class ListGames(Intent):
    def __init__(self, game_master):
        super().__init__('list-games', game_master)

    def execute(self, message, nlp_data):
        str_games_list = 'List of games for {}:'.format(message.user)
        for game in message.user.games:
            str_games_list += '\n\t{}'.format(str(game))
        return str_games_list
