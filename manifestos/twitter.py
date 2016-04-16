import re

from django.conf import settings
import tweepy

TWITTER_CONSUMER_KEY = settings.TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET = settings.TWITTER_CONSUMER_SECRET
TWITTER_ACCESS_KEY = settings.TWITTER_ACCESS_KEY
TWITTER_ACCESS_SECRET = settings.TWITTER_ACCESS_SECRET


class TwitterBot(object):
    """
    Creates tweets for the Digital Manifest Twitter Bot.
    """
    def get_auth(self):
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
        return auth

    def get_api(self):
        auth = self.get_auth()
        return tweepy.API(auth)

    def tweet(self, text):
        if not isinstance(text, str):
            raise NotImplemented('Can only tweet strings.')
        # Escape SMS commands
        pattern = re.compile(
            r'^(ON|OFF|FOLLOW|F|UNFOLLOW|LEAVE|L|STOP|QUIT|END|CANCEL|'
            r'UNSBSCRIBE|ARRET|D|M|RETWEET|RT|SET|WHOIS|W|GET|G|FAV|FAVE|'
            r'FAVORITE|FAVORITE|\*|STATS|SUGGEST|SUG|S|WTF|HELP|INFO|AIDE|'
            r'BLOCK|BLK|REPORT|REP)(\W)(.*)', re.I)
        text = re.sub(pattern, '\\1\u200B\\2\\3', text)

        text = text[:140]
        api = self.get_api()
        api.update_status(status=text)
