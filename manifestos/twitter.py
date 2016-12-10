import re

from django.conf import settings
import tweepy

TWITTER_CONSUMER_KEY = settings.TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET = settings.TWITTER_CONSUMER_SECRET
TWITTER_ACCESS_KEY = settings.TWITTER_ACCESS_KEY
TWITTER_ACCESS_SECRET = settings.TWITTER_ACCESS_SECRET


class TwitterBotException(Exception):
    pass


class TwitterBot(object):
    """
    Creates tweets for the Digital Manifest Twitter Bot.
    """
    @staticmethod
    def get_auth():
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
        return auth

    def get_api(self):
        auth = self.get_auth()
        return tweepy.API(auth)

    def tweet(self, text):
        # Make sure we have legitimate text to tweet
        if not isinstance(text, str):
            raise TwitterBotException('Can only tweet strings.')
        text = text.strip()
        if not text:
            raise TwitterBotException('Text has no content.')

        # Escape SMS commands
        pattern = re.compile(
            r'^(ON|OFF|FOLLOW|F|UNFOLLOW|LEAVE|L|STOP|QUIT|END|CANCEL|'
            r'UNSBSCRIBE|ARRET|D|M|RETWEET|RT|SET|WHOIS|W|GET|G|FAV|FAVE|'
            r'FAVORITE|FAVORITE|\*|STATS|SUGGEST|SUG|S|WTF|HELP|INFO|AIDE|'
            r'BLOCK|BLK|REPORT|REP)(\W)(.*)', re.I)
        text = re.sub(pattern, '\\1\u200B\\2\\3', text)

        # Truncate to 140 characters
        text = text[:140]

        # Tweet
        api = self.get_api()
        api.update_status(status=text)
