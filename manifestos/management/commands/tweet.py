from django.core.management import BaseCommand

from manifestos.twitter import TwitterBot
from manifestos.models import Tweet


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            dest='verbose',
            default=False,
            help='Verbose output',
        )

    def handle(self, *args, **options):
        bot = TwitterBot()
        queryset = Tweet.objects.filter(tweeted=False).order_by('modified')
        if not queryset.count():
            return

        tweet = queryset[0]
        text = tweet.text
        bot.tweet(text)
        tweet.tweeted = True
        tweet.save()
        if options['verbose']:
            print('Tweeted:\n{}'.format(text))
