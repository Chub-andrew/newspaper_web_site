from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import CheckboxSelectMultiple

from catalog.models import Article, Topic, Author


class ArticleForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Article
        fields = "__all__"


class ArticleSearchForm(forms.Form):
    title = (
        forms.CharField(
            max_length=255,
            required=False,
            label="",
            widget=forms.TextInput(attrs={"placeholder": "Search by article"}),
        ),
    )


class TopicForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Topic
        fields = "__all__"


class AuthorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Author
        fields = UserCreationForm.Meta.fields + (
            "username",
            "first_name",
            "last_name",
            "year_of_experience",
        )
