from configparser import ConfigParser


CONFIG_FILE = 'config.ini'

ENVIRONMENT_PRODUCTION = 'production'
ENVIRONMENT_DEVELOP = 'develop'

config = ConfigParser()
config.read(CONFIG_FILE)

environment = config['DEFAULT']['environment']
language = config['DEFAULT']['language']

nlp_service = config['DEFAULT']['nlp_service']

database_engine = config[environment]['database_engine']
database_name = config[environment].get('database_name')
database_user = config[environment].get('database_user')
database_password = config[environment].get('database_password')
database_host = config[environment].get('database_host')
database_port = config[environment].get('database_port')

nlp_service_key = config[nlp_service].get('api_key')
nlp_session_id = config[nlp_service].get('session')

twitter_key = config['twitter']['consumer_key']
twitter_secret = config['twitter']['consumer_secret']
twitter_token = config['twitter']['access_token']
twitter_token_secret = config['twitter']['access_token_secret']

telegram_token = config['telegram']['token']


def is_dev_mode():
    if environment == ENVIRONMENT_DEVELOP:
        return True
    return False
