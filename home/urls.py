from django.urls import path

from home.views import home_page, notifications_page, make_post, comment_post, reply_to_comment, support_post, \
    make_announcement, delete_notification

urlpatterns = (
    path('', home_page, name='home page'),
    path('notifications/', notifications_page, name='notifications'),
    path('delete-notification/<int:notification_id>/', delete_notification, name='delete notification'),
    path('make-post/', make_post, name='make post'),
    path('support/<int:post_id>/', support_post, name='support post'),
    path('comment/<int:post_id>/', comment_post, name='comment post'),
    path('comment/reply/<int:post_id>/<int:comment_id>/', reply_to_comment, name='reply to comment'),
    path('make-announcement/', make_announcement, name='make announcement'),
)
