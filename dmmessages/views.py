from django.shortcuts import render


def inbox_page(request):
    return render(request, 'messages/inbox.html')


def chat_page(request):
    return render(request, 'messages/chat.html')
