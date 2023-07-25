from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ThreadModel, Post


class PollingHandler:
    new_thread = False
    new_post = False
    update_post = False


@receiver(post_save, sender=ThreadModel)
def threads_model_updates(sender, instance, created, **kwargs):
    if created:
        instance.last_post = instance.time_created
        PollingHandler.new_thread = True
        print("thread created")


@receiver(post_save, sender=Post)
def post_model_updates(sender, instance, created, **kwargs):
    if created:
        instance.thread.last_post = instance.time_created
        instance.thread.save()
        PollingHandler.new_post = True
        print("post created")
    else:
        PollingHandler.update_post = True
        print(f"post updated")
