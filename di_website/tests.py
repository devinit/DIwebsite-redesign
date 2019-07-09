from django.test import override_settings
from wagtail.tests.utils import WagtailPageTests
from wagtail.core.models import Site, Page
from di_website.home.models import HomePage
from di_website.users.models import User
from di_website.ourteam.models import OurTeam


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestUserProfileCreation(WagtailPageTests):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@user.com",
            password="testpass",
            first_name="Test",
            last_name="User"
        )

        self.team_page = OurTeam(title="Our Team", slug="team")
        home_page = HomePage.objects.first()
        home_page.add_child(instance=self.team_page)

    def test_user_profile_created(self):
        self.assertEqual(self.user.userprofile.name, "Test User")

    def test_user_profile_200(self):
        response = self.client.get(self.team_page.url)
        self.assertEqual(response.status_code, 200)

    def test_user_profile_appears(self):
        self.user.userprofile.active = True
        self.user.userprofile.save()
        response = self.client.get(self.team_page.url)
        self.assertTrue("Test User" in str(response.content))
