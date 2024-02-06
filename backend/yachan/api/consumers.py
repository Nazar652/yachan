import json
from channels.generic.websocket import AsyncWebsocketConsumer


class CategoryConsumer(AsyncWebsocketConsumer):
    category: str
    category_group_name: str

    async def connect(self):
        self.category = self.scope['url_route']['kwargs']['category']
        self.category_group_name = f"category_{self.category}"

        await self.channel_layer.group_add(self.category_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, text_data=None, bytes_data=None):
        await self.channel_layer.group_discard(self.category_group_name, self.channel_name)

    async def send_threads_update_notification(self, event):
        await self.send(text_data=json.dumps(event))


class ThreadConsumer(AsyncWebsocketConsumer):
    thread_id: str
    thread_group_name: str

    async def connect(self):
        self.thread_id = self.scope['url_route']['kwargs']['thread_id']
        self.thread_group_name = f"thread_{self.thread_id}"

        await self.channel_layer.group_add(self.thread_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, text_data=None, bytes_data=None):
        await self.channel_layer.group_discard(self.thread_group_name, self.channel_name)

    async def send_posts_update_notification(self, event):
        await self.send(text_data=json.dumps(event))

    async def send_thread_update_notification(self, event):
        await self.send(text_data=json.dumps(event))
