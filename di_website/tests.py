from django.test import override_settings
from wagtail.tests.utils import WagtailPageTests
from di_website.home.models import HomePage
from django.contrib.auth.models import User
from di_website.users.models import UserProfile
from di_website.ourteam.models import OurTeamPage


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
        self.userprofile = UserProfile.objects.get(user=self.user)

    def test_user_profile_created(self):
        self.assertEqual(self.userprofile.name, "Test User")

    def test_user_profile_200(self):
        response = self.client.get(self.team_page.url)
        self.assertEqual(response.status_code, 200)

    def test_user_profile_appears(self):
        self.userprofile.active = True
        self.userprofile.save()
        response = self.client.get(self.team_page.url)
        self.assertTrue("Test User" in str(response.content))

    def test_user_page_created(self):
        self.assertEqual(self.userprofile.page.title, self.userprofile.name)

    def test_user_page_renders(self):
        response = self.client.get(self.userprofile.page.url)
        self.assertTrue("Test User" in str(response.content))
