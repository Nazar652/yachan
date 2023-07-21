from django.db.models import *


class Category(Model):
    name = CharField(max_length=40)
    slug = SlugField(max_length=10, unique=True, db_index=True, verbose_name="URL")
    nsfw = BooleanField(default=False)

    def __str__(self):
        return self.name


class ThreadModel(Model):
    subject = CharField(max_length=255)
    text = CharField(max_length=2000)
    author = CharField()
    author_name = CharField(max_length=255, default=None)
    time_created = DateTimeField(auto_now_add=True)
    category = ForeignKey(Category, on_delete=CASCADE)


class Post(Model):
    subject = CharField(max_length=255, default=None)
    text = CharField(max_length=2000)
    updated_text = CharField(max_length=2000, default=None)
    time_created = DateTimeField(auto_now_add=True)
    time_updated = DateTimeField(auto_now=True)
    author = CharField()
    author_name = CharField(max_length=255, default=None)
    thread = ForeignKey(ThreadModel, on_delete=CASCADE)


class ImageModel(Model):
    image = ImageField(upload_to='img/')
    thread = ForeignKey(
        ThreadModel,
        on_delete=CASCADE,
        null=True,
        blank=True,
        limit_choices_to={'post': None},
        related_name='images'
    )
    post = ForeignKey(
        Post,
        on_delete=CASCADE,
        null=True,
        blank=True,
        limit_choices_to={'thread': None},
        related_name='images'
    )
