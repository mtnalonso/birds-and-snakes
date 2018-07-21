from configparser import ConfigParser


CONFIG_FILE = 'config.ini'

ENV_DEV = 'develop'
ENV_PROD = 'production'
ENVIRONMENT = ENV_PROD


class DatabaseConfig:
    def __init__(self, section_config):
        self.config = section_config
        self.engine = self.config['database_engine']
        self.name = self.config.get('database_name')
        self.user = self.config.get('database_user')
        self.password = self.config.get('database_password')


class TwitterConfig:
    def __init__(self, section_config):
        self.config = section_config
        self.key = self.config['consumer_key']
        self.secret = self.config['consumer_secret']
        self.token = self.config['access_token']
        self.token_secret = self.config['access_token_secret']


class TelegramConfig:
    def __init__(self, section_config):
        self.config = section_config
        self.token = self.config.get('token')


class Config:
    def __init__(self, config_file=CONFIG_FILE, environment=ENV_PROD):
        self.config_file = config_file
        self.environment = environment
        self.config = ConfigParser()
        self.config.read(self.config_file)
        self.database = DatabaseConfig(self.config[self.environment])
        self.twitter = TwitterConfig(self.config['twitter'])
        self.telegram = TelegramConfig(self.config['telegram'])

    def is_dev_mode(self):
        if self.environment == ENV_DEV:
            return True
        return False


config = Config()
