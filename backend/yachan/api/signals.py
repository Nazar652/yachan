from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ThreadModel, Post


@receiver(post_save, sender=ThreadModel)
def threads_model_updates(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'thread_{instance.id}',
        {
            'type': 'send.thread.update.notification',
            'data': {
                'thread_id': instance.id,
            }
        })
    async_to_sync(channel_layer.group_send)(
        f'category_{instance.category.slug}',
        {
            'type': 'send.threads.update.notification',
            'data': {
                'category': instance.category.slug,
            }
        })
    if created:
        instance.last_post = instance.time_created


@receiver(post_save, sender=Post)
def post_model_updates(sender, instance, created, **kwargs):
    if created:
        instance.thread.last_post = instance.time_created
        instance.thread.save()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'thread_{instance.thread.id}',
        {
            'type': 'send.posts.update.notification',
            'data': {
                'thread_id': instance.thread.id,
            }
        })


@receiver(post_delete, sender=Post)
def post_model_deletes(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'thread_{instance.thread.id}',
        {
            'type': 'send.posts.update.notification',
            'data': {
                'thread_id': instance.thread.id,
            }
        })


@receiver(post_delete, sender=ThreadModel)
def thread_model_deletes(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'category_{instance.category.slug}',
        {
            'type': 'send.threads.update.notification',
            'data': {
                'category': instance.category.slug,
            }
        })
    async_to_sync(channel_layer.group_send)(
        f'thread_{instance.id}',
        {
            'type': 'send.thread.update.notification',
            'data': {
                'thread_id': instance.id,
            }
        })
