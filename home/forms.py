from django import forms

from home.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('publication_date', 'user')


class PostCreateForm(PostBaseForm):
    pass