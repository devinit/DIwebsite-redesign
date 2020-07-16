from django.contrib.auth.models import User
from django.test import override_settings

from wagtail.tests.utils import WagtailPageTests

from di_website.blog.models import BlogIndexPage, BlogArticlePage
from di_website.home.models import HomePage
from di_website.ourteam.models import OurTeamPage, TeamMemberPage, TeamMemberPageDepartment
from di_website.users.models import Department


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestUserProfileCreation(WagtailPageTests):

    def setUp(self):
        self.team_page = OurTeamPage(title="Our Team", slug="team")
        home_page = HomePage.objects.first()
        home_page.add_child(instance=self.team_page)

        self.user = User.objects.create_user(
            username="testuser",
            email="test@user.com",
            password="testpass",
            first_name="Test",
            last_name="User"
        )

        self.department = Department(name="Data Science")
        self.department.save()

        self.dummy_department = Department(name="A red herring")
        self.dummy_department.save()

        self.team_member_page = TeamMemberPage(
            title="Test user",
            user=self.user,
            name="Test User",
            email="Test.User@Devinit.org",
            telephone="555-867-5309",
            my_story="This is Naphlin Peter Akena",
        )
        self.team_page.add_child(instance=self.team_member_page)
        TeamMemberPageDepartment.objects.create(
            page=self.team_member_page,
            department=self.department
        )

    def test_team_page_200(self):
        response = self.client.get(self.team_page.url)
        self.assertEqual(response.status_code, 200)

    def test_team_page_renders(self):
        response = self.client.get(self.team_page.url)
        self.assertTrue(self.team_member_page.name in str(response.content))

    def test_team_member_page_renders(self):
        response = self.client.get(self.team_member_page.url)
        self.assertTrue(self.team_member_page.name in str(response.content))

    def test_department_filter_positive(self):
        response = self.client.get(self.team_page.url+"?team-filter="+self.department.slug)
        self.assertTrue(self.team_member_page.name in str(response.content))

    def test_department_filter_negative(self):
        response = self.client.get(self.team_page.url+"?team-filter="+self.dummy_department.slug)
        self.assertTrue(self.team_member_page.name not in str(response.content))


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestBlogPages(WagtailPageTests):
    def setUp(self):
        self.blog_index_page = BlogIndexPage(title="Test Blog Index Page", slug="blog")
        home_page = HomePage.objects.first()
        home_page.add_child(instance=self.blog_index_page)

        self.blog_article_page = BlogArticlePage(title="Test Blog Article", slug="test")
        self.blog_index_page.add_child(instance=self.blog_article_page)

    def test_blog_index_page_200(self):
        response = self.client.get(self.blog_index_page.url)
        self.assertEqual(response.status_code, 200)

    def test_blog_index_page_renders(self):
        response = self.client.get(self.blog_index_page.url)
        self.assertTrue(self.blog_index_page.title in str(response.content))

    def test_blog_article_page_200(self):
        response = self.client.get(self.blog_article_page.url)
        self.assertEqual(response.status_code, 200)

    def test_blog_article_page_renders(self):
        response = self.client.get(self.blog_article_page.url)
        self.assertTrue(self.blog_article_page.title in str(response.content))
