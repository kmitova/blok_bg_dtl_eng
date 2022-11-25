from django.urls import path

from dmmessages.views import inbox_page, chat_page

urlpatterns = (
    path('', inbox_page, name='inbox'),
    path('chat/', chat_page, name="chat"),
)