from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_slug = self.scope['url_route']['kwargs']['chat_slug']
        self.chat_group_slug = 'chat_%s' % self.chat_slug

        await self.channel_layer.group_add(
            self.chat_slug,
            self.chat_group_slug
        )

        await self.accept()


    async def disconnect(self):
        pass
