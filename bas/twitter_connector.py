import logging
import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, \
        ACCESS_TOKEN_SECRET

logger = logging.getLogger(__name__)


class TwitterConnector:
    def __init__(self, inbox_queue):
        self.username = "birdsandsnakes"
        self.auth = None
        self.api = None
        self.active = False
        self.listener = None

        self.__load_auth()

    def __load_auth(self):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def publish_tweet(self, tweet_content):
        self.api.update_status(status=tweet_content)

    def send_reply(self, reply_content):
        raise NotImplementedError

    def init_listener(self):
        self.listener = TwitterListener(self.inbox_queue)
        self.stream = tweepy.Stream(auth=self.auth, listener=self.listener)
        self.stream.filter(track=[self.username], async=True)
        self.active = True

    def stop_listener(self):
        self.listener.stop()
        self.active = False


class TwitterListener(tweepy.StreamListener):
    def __init__(self, inbox_queue):
        super().__init__()
        self.inbox_queue = inbox_queue

    def on_status(self, status):
        if self.running:
            self.__get_tweet_from_status(status)
            return True
        else:
            return False

    def __get_tweet_from_status(self, status):
        logger.info('@[{}]: {}'.format(status.user.screen_name, status.text))
        self.inbox_queue.put(status)

    def on_error(self, status_code):
        if status_code == 420:
            logger.error('[420]:\tEnhance Your Calm!')
            return False

    def stop(false):
        self.running = False
