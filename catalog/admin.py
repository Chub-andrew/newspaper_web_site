from django.contrib import admin

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
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'year_of_experience',
        'password',
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',

    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )
    raw_id_fields = ('groups', 'user_permissions')
