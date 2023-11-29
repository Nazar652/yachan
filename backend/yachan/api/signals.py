from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ThreadModel, Post


@receiver(post_save, sender=ThreadModel)
def threads_model_updates(sender, instance, created, **kwargs):
    if created:
        instance.last_post = instance.time_created
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'thread',
            {
                'type': 'send.new.thread.notification',
                'data': {
                    'category': instance.category.slug,
                }
            })


@receiver(post_save, sender=Post)
def post_model_updates(sender, instance, created, **kwargs):
    if created:
        instance.thread.last_post = instance.time_created
        instance.thread.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'post',
            {
                'type': 'send.new.post.notification',
                'data': {
                    'thread_id': instance.thread.id,
                }
            })

    else:
        print(f"post updated")
