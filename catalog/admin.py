from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Topic, Article, Author


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'topic',
        'title',
        'slug',
        'published_at',
        'short_content',
        'content',
        'main_image',
        'created_at',
        'updated_at',
    )
    list_filter = ('topic', 'published_at', 'created_at', 'updated_at')
    raw_id_fields = ('publishers', 'tags')
    search_fields = ('slug',)
    date_hierarchy = 'created_at'


@admin.register(Author)
class AuthorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("year_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("year_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "year_of_experience",
                    )
                },
            ),
        )
    )
