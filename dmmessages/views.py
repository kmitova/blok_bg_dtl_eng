from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from dmmessages.models import Chat, ChatMessage

UserModel = get_user_model()
@login_required
def go_to_chat(request, slug):
    """
    - get username of logged in user
    - get username of other user
    - slug = username1+username2
    - check if such chat exists by the slug: if not, make one and open it
    - else: open the exisiting one
    """

    current_user = request.user
    # other_user =
    pass


@login_required
def inbox_page(request):
    user = request.user
    messages = ChatMessage.get_messages(user=user)
    active_direct = None
    directs = None
    context = {}

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = ChatMessage.objects.filter(user=user, recipient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0

        context = {
            'directs': directs,
            'messages': messages,
            'active_direct': active_direct
        }

    return render(request, 'messages/inbox.html', context)


@login_required
def send_message(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')
    print(body)
    if request.method == 'POST':
        to_user = UserModel.objects.get(username=to_user_username)
        ChatMessage.send_message(from_user, to_user, body)
        return redirect('chat', username=to_user_username)
    else:
        return HttpResponseBadRequest()


@login_required
def chat_page(request, username):
    user = request.user
    messages = ChatMessage.get_messages(user=user)
    active_direct = username
    directs = ChatMessage.objects.filter(user=user, recipient__username=username)
    directs.update(is_read=True)
    recipient = UserModel.objects.filter(username=username).get()
    context = {}

    # if messages:
    #     message = messages[0]
    #     active_direct = message['user'].username
    #     directs = ChatMessage.objects.filter(user=user, recipient=message['user'])
    #     directs.update(is_read=True)

    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0

    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
        'recipient': recipient
    }

    return render(request, 'messages/chat.html', context)
