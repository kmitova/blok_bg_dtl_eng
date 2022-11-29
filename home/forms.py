from django import forms

from home.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('publication_date', 'user')


class PostCreateForm(PostBaseForm):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)