import json
from channels.generic.websocket import AsyncWebsocketConsumer


class PostConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("post", self.channel_name)
        await self.accept()

    async def disconnect(self, text_data=None, bytes_data=None):
        await self.channel_layer.group_discard("post", self.channel_name)

    async def send_new_post_notification(self, event):
        await self.send(text_data=json.dumps(event))


class ThreadConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("thread", self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        await self.channel_layer.group_discard("thread", self.channel_name)

    async def send_new_thread_notification(self, event):
        await self.send(text_data=json.dumps(event))
