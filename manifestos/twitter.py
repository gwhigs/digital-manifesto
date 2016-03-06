import tweepy

from django.conf import settings


TWITTER_CONSUMER_KEY = settings.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = settings.get('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_KEY = settings.get('TWITTER_ACCESS_KEY')
TWITTER_ACCESS_SECRET = settings.get('TWITTER_ACCESS_SECRET')


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

        text = text[:140]
        api = self.get_api()
        api.update_status(status=text)
