from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from taggit.managers import TaggableManager
from django.contrib.auth.models import AbstractUser


class Topic(models.Model):
    """
    Topic model to represent a category or subject area of articles.
    """
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True)
    image = models.ImageField(max_length=300, upload_to="topics/images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (f"Topic id={self.pk}, name={self.name}, slug={self.slug}, "
                f"created_at={self.created_at}, updated_at={self.updated_at}")


class Article(models.Model):
    """
    Article model to represent individual articles with their content and metadata.
    """
    topic = models.ForeignKey(
        Topic,
        verbose_name="Topic",
        on_delete=models.RESTRICT,
        db_index=True,
        related_name="articles"
    )
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title", unique_for_date="published_at")
    published_at = models.DateField(db_index=True, blank=True, null=True)
    short_content = models.TextField(max_length=600)
    content = models.TextField()
    main_image = models.ImageField(max_length=300, blank=True, null=True, upload_to="articles/images/%Y/%m")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="articles")
    tags = TaggableManager(blank=True)

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return (f"Article id={self.pk}, title={self.title}, published_at={self.published_at}, "
                f"created_at={self.created_at}, updated_at={self.updated_at}")


class Author(AbstractUser):
    """
    Author model to extend the default user model with additional fields.
    """
    year_of_experience = models.IntegerField(blank=False,)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('catalog:author_articles', args=[str(self.id)])
