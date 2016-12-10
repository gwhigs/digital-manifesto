import re

from django.conf import settings
import tweepy

# Twitter API Credentials
TWITTER_CONSUMER_KEY = settings.TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET = settings.TWITTER_CONSUMER_SECRET
TWITTER_ACCESS_KEY = settings.TWITTER_ACCESS_KEY
TWITTER_ACCESS_SECRET = settings.TWITTER_ACCESS_SECRET


class TwitterBotException(Exception):
    pass


def escape_sms_commands(text):
    pattern = re.compile(
        r'^(ON|OFF|FOLLOW|F|UNFOLLOW|LEAVE|L|STOP|QUIT|END|CANCEL|'
        r'UNSBSCRIBE|ARRET|D|M|RETWEET|RT|SET|WHOIS|W|GET|G|FAV|FAVE|'
        r'FAVORITE|FAVORITE|\*|STATS|SUGGEST|SUG|S|WTF|HELP|INFO|AIDE|'
        r'BLOCK|BLK|REPORT|REP)(\W)(.*)', re.I)
    text = re.sub(pattern, '\\1\u200B\\2\\3', text)
    return text


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

    @staticmethod
    def clean_text(text):
        """
        Prepares a string to be tweeted.
        """
        # Make sure we have a string
        if not isinstance(text, str):
            raise TwitterBotException('Can only tweet strings.')

        # Text should have content
        text = text.strip()
        if not text:
            raise TwitterBotException('Text has no content.')

        # Escape SMS commands
        text = escape_sms_commands(text)

        # Truncate to 140 characters
        text = text[:140]
        return text

    def tweet(self, text):
        # Prepare our text for tweeting (truncate to 140 chars, etc.)
        text = self.clean_text(text)

        # Send our tweet
        api = self.get_api()
        api.update_status(status=text)
