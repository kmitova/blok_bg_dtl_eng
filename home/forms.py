from django import forms

from home.models import Post, Comment, Reply, Announcement


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
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'placeholder': 'Add a comment...',
                }
            )}


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'placeholder': 'Add a reply...',
                }
            )}


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'content')
