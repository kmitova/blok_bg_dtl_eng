from django import forms

from home.models import Post, Comment, Reply, Announcement, SupportPost


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('publication_date', 'user')


class PostCreateForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def save(self, commit=True):
        if commit:
            # self.instance.comments.clear()
            SupportPost.objects.filter(id=self.instance.id).delete()
            Comment.objects.filter(post_id=self.instance.id).delete()

            self.instance.delete()
        else:
            pass
        return self.instance


class PostEditForm(PostBaseForm):
    pass
    # class Meta:
    #     model = Post
    #     exclude = ('publication_date', 'photo')
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
