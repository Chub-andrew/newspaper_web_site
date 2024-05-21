from django.urls import path

from catalog.views import (
    index,
    AuthorArticleListView,
    AuthorListView,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    TopicListView,
    TopicCreateView,
    AuthorCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "articles/",
        ArticleListView.as_view(),
        name="article_list",
    ),
    path(
        "articles/<int:pk>/",
        ArticleDetailView.as_view(),
        name="article_detail"
    ),
    path(
        "articles/create/",
        ArticleCreateView.as_view(),
        name="article_create",
    ),
    path(
        "articles/<int:pk>/update/",
        ArticleUpdateView.as_view(),
        name="article_update",
    ),
    path(
        "authors/",
        AuthorListView.as_view(),
        name="author-list"
    ),
    path(
        "authors/<int:pk>/",
        AuthorArticleListView.as_view(),
        name="author_articles"
    ),
    path(
        "authors/create/",
        AuthorCreateView.as_view(),
        name="author_create"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic_list",
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic_create",
    ),
]


app_name = "catalog"
