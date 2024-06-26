from django.db.models import *


class Category(Model):
    name = CharField(max_length=40)
    description = CharField(max_length=255, null=True, blank=True)
    slug = SlugField(max_length=10, unique=True, db_index=True, verbose_name="URL")
    nsfw = BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['slug']


class ThreadModel(Model):
    subject = CharField(max_length=255)
    text = CharField(max_length=2000)
    updated_text = CharField(max_length=2000, null=True, default=None)
    author = CharField()
    author_name = CharField(max_length=255, null=True, default=None)
    time_created = DateTimeField(auto_now_add=True)
    last_post = DateTimeField(auto_now=True)
    category = ForeignKey(Category, on_delete=CASCADE, to_field='slug')

    class Meta:
        ordering = ['-last_post']


class Post(Model):
    subject = CharField(max_length=255, null=True, default=None)
    text = CharField(max_length=2000)
    updated_text = CharField(max_length=2000, null=True, default=None)
    time_created = DateTimeField(auto_now_add=True)
    time_updated = DateTimeField(auto_now=True)
    author = CharField()
    author_name = CharField(max_length=255, null=True, default=None)
    thread = ForeignKey(ThreadModel, on_delete=CASCADE)
    is_op = BooleanField(default=False)

    class Meta:
        ordering = ['-time_created']


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
