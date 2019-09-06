"""Management command that fixes imported WP content."""

import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from di_website.blog.models import BlogArticlePage
from di_website.ourteam.models import TeamMemberPage


class Command(BaseCommand):
    """Management command that imports news from a JSON file."""

    help = 'Import news given a JSON file.'

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('blogs_file', nargs='?', type=str, default=os.path.join(settings.BASE_DIR, 'migrated_content/di_blogs.json'))

    def handle(self, *args, **options):
        """Implement the command handler."""

        with open(options['blogs_file']) as blogs_file:
            blog_datasets = json.load(blogs_file)
            for blog_dataset in blog_datasets:
                slug = blog_dataset['url'].split('/')[-2]
                blog_check = BlogArticlePage.objects.filter(slug=slug)
                if blog_check:
                    blog_page = blog_check.first()

                    other_authors = []
                    author_names = blog_dataset["author"]
                    if author_names:
                        author_name = author_names[0]
                        internal_author_page_qs = TeamMemberPage.objects.filter(name=author_name)
                        if internal_author_page_qs:
                            blog_page.internal_author_page = internal_author_page_qs.first()
                        else:
                            author_obj = {"type": "external_author", "value": {"name": author_name, "title": "", "photograph": None, "page": ""}}
                            other_authors.append(author_obj)
                    if len(author_names) > 1:
                        for author_name in author_names[1:]:
                            internal_author_page_qs = TeamMemberPage.objects.filter(name=author_name)
                            if internal_author_page_qs:
                                author_obj = {"type": "internal_author", "value": internal_author_page_qs.first().pk}
                            else:
                                author_obj = {"type": "external_author", "value": {"name": author_name, "title": "", "photograph": None, "page": ""}}
                            other_authors.append(author_obj)
                    if other_authors:
                        blog_page.other_authors = json.dumps(other_authors)

                    blog_page.save_revision().publish()

        self.stdout.write(self.style.SUCCESS('Successfully fixed blogs.'))
