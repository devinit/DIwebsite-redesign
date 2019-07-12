from django.test import override_settings
from wagtail.tests.utils import WagtailPageTests
from di_website.home.models import HomePage
from django.contrib.auth.models import User
from di_website.ourteam.models import OurTeamPage, TeamMemberPage


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

        self.team_member_page = TeamMemberPage(
            title="Test user",
            user=self.user,
            name="Test User",
            email="Test.User@Devinit.org",
            telephone="555-867-5309"
        )
        self.team_page.add_child(instance=self.team_member_page)

    def test_team_page_200(self):
        response = self.client.get(self.team_page.url)
        self.assertEqual(response.status_code, 200)

    def test_team_page_renders(self):
        response = self.client.get(self.team_page.url)
        self.assertTrue("Test User" in str(response.content))

    def test_team_member_page_renders(self):
        response = self.client.get(self.team_member_page.url)
        self.assertTrue("Test User" in str(response.content))
