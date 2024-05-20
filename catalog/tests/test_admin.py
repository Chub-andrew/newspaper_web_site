from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="password1234",
            year_of_experience=0,
        )
        self.client.force_login(self.admin_user)
        self.author = get_user_model().objects.create_user(
            username="author",
            password="test_password",
            year_of_experience=10,
        )

    def test_author_listed(self):
        """Test that authors are listed on the author admin page"""
        url = reverse("admin:catalog_author_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.author.username)
        self.assertContains(res, self.author.year_of_experience)

    def test_author_change_page(self):
        """Test that the author edit page works"""
        url = reverse("admin:catalog_author_change", args=[self.author.id])
        res = self.client.get(url)
        self.assertContains(res, self.author.username)
        self.assertContains(res, self.author.year_of_experience)

    def test_create_author_page(self):
        """Test that the create author page works"""
        url = reverse("admin:catalog_author_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
