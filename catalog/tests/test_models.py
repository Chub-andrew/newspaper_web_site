from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import Author, Article, Topic


class ArticleTestCase(TestCase):
    def test_article_str(self):
        topic = Topic.objects.create(
            name="test_name",
        )
        article = Article.objects.create(title="test", topic=topic)
        self.assertEqual(str(article), article.title)

    def test_author_str(self):
        author = get_user_model().objects.create(
            username="test",
            first_name="test_first",
            last_name="test_last",
            year_of_experience=10,
        )
        self.assertEqual(
            str(author),
            f"{author.username} ("
            f"{author.first_name} "
            f"{author.last_name}"
            f")"
        )

    def test_topic_str(self):
        topic = Topic.objects.create(
            name="test_name",
        )
        self.assertEqual(str(topic), f"{topic.name}")
