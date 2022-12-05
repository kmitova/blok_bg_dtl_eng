from django.urls import path

from dmmessages.views import inbox_page, chat_page, send_message

urlpatterns = (
    path('', inbox_page, name='inbox'),
    path('chat/<username>/', chat_page, name="chat"),
    path('send/', send_message, name='send message')
)