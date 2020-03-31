"""Management command that adds all news story page publication dates."""


from django.core.management.base import BaseCommand

from di_website.news import NewsStoryPage


class Command(BaseCommand):
    """Management command adds all news story page publication dates."""

    help = 'Add all news story page publication dates'

    def handle(self, *args, **options):

        all_news = NewsStoryPage.objects.live()
        for news_story in all_news:
            news_story.publication_date = news_story.first_published_at
            news_story.save_revision().publish()

        self.stdout.write(self.style.SUCCESS('Called successfully'))
