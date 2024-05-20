from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Topic


class PublicTopicTest(TestCase):
    def test_login_required(self):
        url = reverse("catalog:topic_list")
        res = self.client.get(url)
        self.assertNotEquals(res.status_code, 200)


class PrivateTopicTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="text",
            password="password",
            year_of_experience=0,
        )
        self.client.force_login(self.user)

    def test_retrieve_topic(self):
        Topic.objects.create(name="Test Topic")
        url = reverse("catalog:topic_list")
        res = self.client.get(url)
        self.assertEquals(res.status_code, 200)
        topics = Topic.objects.all()
        self.assertEquals(
            list(res.context["topics"]),
            list(topics),
        )
        self.assertTemplateUsed(res, "catalog/topic_list.html")
