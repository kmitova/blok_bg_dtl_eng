

from django.contrib import admin

from home.models import Post, Comment, Reply, SupportPost, Notification, Announcement

LIST_FILTER = ('publication_date', 'user')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('publication_date', 'user')
    list_filter = LIST_FILTER



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('publication_date', 'post_id', 'user')
    list_filter = LIST_FILTER


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('publication_date', 'comment', 'user')
    list_filter = LIST_FILTER


@admin.register(SupportPost)
class SupportPostAdmin(admin.ModelAdmin):
    list_display = ('related_post',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('date', 'user',)
    list_filter = ('date',)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    search_fields = ('title__startswith',)