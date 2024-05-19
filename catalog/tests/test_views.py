from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class PublicTopicTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        url = reverse('catalog:topic_list')
        res = self.client.get(url)
        self.assertNotEquals(res.status_code, 200)
