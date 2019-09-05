"""Management command that imports WP content from JSON files."""

import datetime
from io import BytesIO
import json
import os
import PIL.Image
import pytz

from django.conf import settings
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from di_website.blog.models import BlogArticlePage, BlogIndexPage
from di_website.news.models import NewsIndexPage, NewsStoryPage
from di_website.ourteam.models import OurTeamPage, TeamMemberPage, TeamMemberPageDepartment
from di_website.users.models import Department, JobTitle
from di_website.publications.models import PublicationIndexPage, LegacyPublicationPage, PublicationType

from wagtail.contrib.redirects.models import Redirect
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
        parser.add_argument('pubs_file', nargs='?', type=str, default=os.path.join(settings.BASE_DIR, 'migrated_content/di_pubs.json'))

    def handle(self, *args, **options):
        """Implement the command handler."""

        our_team_page = OurTeamPage.objects.live().first()
        news_index_page = NewsIndexPage.objects.live().first()
        blog_index_page = BlogIndexPage.objects.live().first()
        publication_index_page = PublicationIndexPage.objects.live().first()

        if our_team_page is not None:
            with open(options['staff_file']) as staff_file:
                staff_datasets = json.load(staff_file)
                for staff_dataset in staff_datasets:
                    slug = staff_dataset['url'].split('/')[-2]
                    staff_name = staff_dataset["name"]
                    img_title = "{} profile picture".format(staff_name)
                    img_check = Image.objects.filter(title=img_title)

                    if img_check:
                        img = img_check.first()
                    elif staff_dataset["img"] != "":
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

                    job_title_name = staff_dataset["position"]
                    job_title, _ = JobTitle.objects.get_or_create(name=job_title_name)

                    page_check = TeamMemberPage.objects.filter(slug=slug)
                    if not page_check:
                        staff_page = TeamMemberPage(
                            title=staff_name,
                            slug=slug,
                            name=staff_name,
                            image=img,
                            position=job_title,
                            my_story=staff_dataset["body"]
                        )
                        our_team_page.add_child(instance=staff_page)
                        staff_page.save_revision().publish()
                        Redirect.objects.create(
                            site=staff_page.get_site(),
                            old_path="/post/people/{}".format(slug),
                            redirect_page=staff_page
                        )

                        departments = staff_dataset["department"].split()
                        department_names = [dept.replace("-", " ").capitalize() for dept in departments]
                        for department_name in department_names:
                            department, _ = Department.objects.get_or_create(name=department_name)
                            TeamMemberPageDepartment.objects.create(
                                page=staff_page,
                                department=department
                            )
        self.stdout.write(self.style.SUCCESS('Successfully imported staff profiles.'))

        if blog_index_page is not None:
            with open(options['blogs_file']) as blogs_file:
                blog_datasets = json.load(blogs_file)
                for blog_dataset in blog_datasets:
                    slug = blog_dataset['url'].split('/')[-2]
                    blog_check = BlogArticlePage.objects.filter(slug=slug)
                    if not blog_check and blog_dataset['body'] != "":
                        blog_page = BlogArticlePage(
                            title=blog_dataset['title'],
                            slug=slug,
                            hero_text=blog_dataset['description'],
                            body=json.dumps([{'type': 'paragraph_block', 'value': blog_dataset['body']}]),
                        )
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
                        blog_index_page.add_child(instance=blog_page)
                        blog_page.save_revision().publish()
                        blog_page.first_published_at = pytz.utc.localize(datetime.datetime.strptime(blog_dataset['date'], "%d %b %Y"))
                        blog_page.save_revision().publish()
                        Redirect.objects.create(
                            site=blog_page.get_site(),
                            old_path="/post/{}".format(slug),
                            redirect_page=blog_page
                        )

        self.stdout.write(self.style.SUCCESS('Successfully imported blogs.'))

        if news_index_page is not None:
            with open(options['news_file']) as news_file:
                news_datasets = json.load(news_file)
                for news_dataset in news_datasets:
                    slug = news_dataset['url'].split('/')[-2].replace("%e2%88%92", "-")
                    news_check = NewsStoryPage.objects.filter(slug=slug)
                    if not news_check and news_dataset['body'] != "":
                        news_page = NewsStoryPage(
                            title=news_dataset['title'],
                            slug=slug,
                            hero_text=news_dataset['description'],
                            body=json.dumps([{'type': 'paragraph_block', 'value': news_dataset['body']}]),
                        )
                        news_index_page.add_child(instance=news_page)
                        news_page.save_revision().publish()
                        news_page.first_published_at = pytz.utc.localize(datetime.datetime.strptime(news_dataset['date'], "%d %b %Y"))
                        news_page.save_revision().publish()
                        try:
                            Redirect.objects.create(
                                site=news_page.get_site(),
                                old_path="/post/{}".format(news_dataset['url'].split('/')[-2]),
                                redirect_page=news_page
                            )
                        except IntegrityError:
                            pass  # Sometimes a post was simultaneously news and a blog. In these cases retain both but don't have two redirects

        self.stdout.write(self.style.SUCCESS('Successfully imported news.'))

        if publication_index_page is not None:
            with open(options['pubs_file']) as pubs_file:
                publication_datasets = json.load(pubs_file)
                for publication_dataset in publication_datasets:

                    publication_type, _ = PublicationType.objects.get_or_create(name=publication_dataset['format'].split(";")[0])

                    slug = publication_dataset['url'].split('/')[-2]
                    pub_check = LegacyPublicationPage.objects.filter(slug=slug)
                    if not pub_check and publication_dataset['body'] != "":
                        pub_page = LegacyPublicationPage(
                            title=publication_dataset['title'],
                            slug=slug,
                            hero_text=publication_dataset['description'],
                            content=publication_dataset['body'],
                            publication_type=publication_type
                        )
                        authors = []
                        author_names = publication_dataset["author"]
                        for author_name in author_names:
                            internal_author_page_qs = TeamMemberPage.objects.filter(name=author_name)
                            if internal_author_page_qs:
                                author_obj = {"type": "internal_author", "value": internal_author_page_qs.first().pk}
                            else:
                                author_obj = {"type": "external_author", "value": {"name": author_name, "title": "", "photograph": None, "page": ""}}
                            authors.append(author_obj)
                        if authors:
                            pub_page.other_authors = json.dumps(authors)
                        publication_index_page.add_child(instance=pub_page)
                        pub_page.save_revision().publish()
                        pub_page.published_date = pytz.utc.localize(datetime.datetime.strptime(publication_dataset['date'], "%d %b %Y"))
                        pub_page.save_revision().publish()
                        Redirect.objects.create(
                            site=pub_page.get_site(),
                            old_path="/post/{}".format(slug),
                            redirect_page=pub_page
                        )

        self.stdout.write(self.style.SUCCESS('Successfully imported publications.'))
