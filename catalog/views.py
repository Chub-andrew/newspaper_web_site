from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import generic

from .models import Author, Topic, Article
from .forms import ArticleForm, TopicForm, AuthorCreationForm, ArticleSearchForm


def index(request: HttpRequest):
    num_authors = Author.objects.count()
    num_topics = Topic.objects.count()
    num_articles = Article.objects.count()
    context = {
        'num_authors': num_authors,
        'num_topics': num_topics,
        'num_articles': num_articles,
    }
    return render(request, "catalog/index.html", context=context)


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author


class AuthorArticleListView(ListView):
    model = Article
    template_name = 'catalog/author_articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(publishers__id=self.kwargs['pk'])


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    # template_name = "catalog/article_list.html"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        query = self.request.GET.get("title", "")
        context["search_form"] = ArticleSearchForm()
        return context


class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article


class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("catalog:article_list")
    template_name = "catalog/article_form.html"


class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("catalog:article_list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topics"
    template_name = "catalog/topic_list.html"
    paginate_by = 6


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    success_url = reverse_lazy("catalog:topic_list")
    form_class = TopicForm


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorCreationForm
    success_url = reverse_lazy('catalog:author-list')
