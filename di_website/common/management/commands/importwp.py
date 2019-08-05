"""Management command that imports WP content from JSON files."""

import datetime
from io import BytesIO
import json
import os
import PIL.Image
import pytz

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from di_website.blog.models import BlogArticlePage, BlogIndexPage
from di_website.news.models import NewsIndexPage, NewsStoryPage
from di_website.ourteam.models import OurTeamPage, TeamMemberPage
from di_website.users.models import Department, JobTitle

from wagtail.images.models import Image


class Command(BaseCommand):
    """Management command that imports news from a JSON file."""

    help = 'Import news given a JSON file.'

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('staff_file', nargs='?', type=str, default=os.path.join(settings.BASE_DIR, 'migrated_content/di_staff.json'))
        parser.add_argument('blogs_file', nargs='?', type=str, default=os.path.join(settings.BASE_DIR, 'migrated_content/di_blogs.json'))
        parser.add_argument('news_file', nargs='?', type=str, default=os.path.join(settings.BASE_DIR, 'migrated_content/di_news.json'))
        parser.add_argument('img_folder', nargs='?', type=str, default=os.path.join(settings.BASE_DIR, 'migrated_content/staff_photos'))
        # parser.add_argument('pubs_file', nargs='+', type=str, default=os.path.join(settings.BASE_DIR, 'migrated_content/di_pubs.json'))

    def handle(self, *args, **options):
        """Implement the command handler."""

        our_team_page = OurTeamPage.objects.live().first()
        news_index_page = NewsIndexPage.objects.live().first()
        blog_index_page = BlogIndexPage.objects.live().first()

        if our_team_page is not None:
            with open(options['staff_file']) as staff_file:
                staff_datasets = json.load(staff_file)
                for staff_dataset in staff_datasets:
                    staff_name = staff_dataset["name"]
                    img_title = "{} profile picture".format(staff_name)
                    img_check = Image.objects.filter(title=img_title)

                    if staff_dataset["img"] != "" and not img_check:
                        img_filename = staff_dataset["img"].split('/')[-1]
                        _, img_ext = os.path.splitext(img_filename)
                        if img_ext.lower() == ".jpg":
                            img_ext = ".jpeg"
                        img_path = os.path.join(options['img_folder'], img_filename)
                        f = BytesIO()
                        pil_img = PIL.Image.open(img_path)
                        pil_img.save(f, img_ext[1:])
                        img = Image(
                            title=img_title,
                            file=ImageFile(f, name=img_filename)
                        )
                        img.save()
                    else:
                        img = None

                    department_name = staff_dataset["department"].replace("-", " ").capitalize()
                    department, _ = Department.objects.get_or_create(name=department_name)

                    job_title_name = staff_dataset["position"]
                    job_title, _ = JobTitle.objects.get_or_create(name=job_title_name)

                    page_check = TeamMemberPage.objects.filter(title=staff_name)
                    if not page_check:
                        staff_page = TeamMemberPage(
                            title=staff_name,
                            slug=slugify(staff_name),
                            name=staff_name,
                            image=img,
                            department=department,
                            position=job_title,
                            my_story=staff_dataset["body"]
                        )
                        our_team_page.add_child(instance=staff_page)
                        staff_page.save_revision().publish()

        if blog_index_page is not None:
            with open(options['blogs_file']) as blogs_file:
                blog_datasets = json.load(blogs_file)
                for blog_dataset in blog_datasets:
                    blog_check = BlogArticlePage.objects.filter(title=blog_dataset['title'])
                    if not blog_check:
                        blog_page = BlogArticlePage(
                            title=blog_dataset['title'],
                            hero_text=blog_dataset['description'],
                            body=json.dumps([{'type': 'paragraph', 'value': blog_dataset['body']}]),
                        )
                        author_names = blog_dataset["author"]
                        if author_names:
                            author_name = author_names[0]
                        else:
                            author_name = None
                        internal_author_page_qs = TeamMemberPage.objects.filter(name=author_name)
                        if internal_author_page_qs:
                            blog_page.internal_author_page = internal_author_page_qs.first()
                        else:
                            blog_page.external_author_name = author_name
                        blog_index_page.add_child(instance=blog_page)
                        blog_page.save_revision().publish()
                        blog_page.first_published_at = datetime.datetime.strptime(blog_dataset['date'], "%d %b %Y")
                        blog_page.save()
        # if news_index_page is not None and event_index_page is not None:
        #     with open(options['json_file'][0]) as json_file:
        #         json_data = json.load(json_file)
        #
        #         for page_data in json_data:
        #             page_slug = page_data['link'].split("/")[-1]
        #             if page_data["type"] == "news":
        #                 try:
        #                     news_page = NewsPage(
        #                         title_en=page_data["title"],
        #                         slug_en=page_slug,
        #                         heading_en=page_data["title"],
        #                         content_editor_en=json.dumps([{'type': 'paragraph', 'value': page_data["content"]}]),
        #                         title=page_data["title"],
        #                         slug=page_slug,
        #                         heading=page_data["title"],
        #                         content_editor=json.dumps([{'type': 'paragraph', 'value': page_data["content"]}]),
        #                         date=datetime.datetime.strptime(page_data["date"], "%Y-%m-%d").date()
        #                     )
        #                     news_index_page.add_child(instance=news_page)
        #                     news_page.save_revision().publish()
        #                     self.stdout.write(self.style.SUCCESS("News: " + page_data["title"]))
        #                 except ValidationError:
        #                     self.stdout.write(self.style.NOTICE("News: " + page_data["title"]))
        #             else:
        #                 try:
        #                     event_page = EventPage(
        #                         title_en=page_data["title"],
        #                         slug_en=page_slug,
        #                         heading_en=page_data["title"],
        #                         content_editor_en=json.dumps([{'type': 'paragraph', 'value': page_data["content"]}]),
        #                         title=page_data["title"],
        #                         slug=page_slug,
        #                         heading=page_data["title"],
        #                         content_editor=json.dumps([{'type': 'paragraph', 'value': page_data["content"]}]),
        #                         date_start=datetime.datetime.strptime(page_data["date"], "%Y-%m-%d").replace(tzinfo=pytz.UTC),
        #                         date_end=datetime.datetime.strptime(page_data["date"], "%Y-%m-%d").replace(tzinfo=pytz.UTC)
        #                     )
        #                     event_index_page.add_child(instance=event_page)
        #                     event_page.save_revision().publish()
        #                     self.stdout.write(self.style.SUCCESS("Event: " + page_data["title"]))
        #                 except ValidationError:
        #                     self.stdout.write(self.style.NOTICE("Event: " + page_data["title"]))
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully imported news and events.'))
