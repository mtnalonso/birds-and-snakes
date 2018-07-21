from configparser import ConfigParser


CONFIG_FILE = 'config.ini'

ENV_DEV = 'develop'
ENV_PROD = 'production'
ENVIRONMENT = ENV_PROD

config = ConfigParser()
config.read(CONFIG_FILE)

database_engine = config[ENVIRONMENT]['database_engine']
database_name = config[ENVIRONMENT].get('database_name')
database_user = config[ENVIRONMENT].get('database_user')
database_password = config[ENVIRONMENT].get('database_password')

twitter_key = config['twitter']['consumer_key']
twitter_secret = config['twitter']['consumer_secret']
twitter_token = config['twitter']['access_token']
twitter_token_secret = config['twitter']['access_token_secret']

telegram_token = config['telegram']['token']


def is_dev_mode():
    if ENVIRONMENT == ENV_DEV:
        return True
    return False
