from datetime import datetime
import re

from .models import *

from rest_framework.serializers import ModelSerializer, ListField
from rest_framework.fields import ImageField


def img_name_to_date(img_name):
    name = ''.join(re.split(r'[- :]', str(datetime.now()))).replace('.', '-')
    image_format = img_name.split('.')[-1]
    return name + '.' + image_format


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImageModelSerializer(ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'


class ThreadSerializer(ModelSerializer):
    images = ImageModelSerializer(many=True, read_only=True)
    uploaded_images = ListField(
        child=ImageField(allow_empty_file=False),
        allow_empty=False,
        max_length=5,
        write_only=True
    )

    class Meta:
        model = ThreadModel
        fields = ["id", "subject", "text", "author", "author_name", "time_created", "category", "images",
                  "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        thread = ThreadModel.objects.create(**validated_data)
        for image in uploaded_images:
            image.name = img_name_to_date(image.name)
            ImageModel.objects.create(thread=thread, image=image)

        return thread


class PostSerializer(ModelSerializer):
    images = ImageModelSerializer(many=True, read_only=True)
    uploaded_images = ListField(
        child=ImageField(allow_empty_file=False),
        allow_empty=False,
        max_length=5,
        write_only=True
    )

    class Meta:
        model = Post
        fields = ["id", "subject", "text", "updated_text", "time_created", "time_updated", "author", "author_name",
                  "thread", "images", "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        post = Post.objects.create(**validated_data)
        for image in uploaded_images:
            image.name = img_name_to_date(image.name)
            ImageModel.objects.create(thread=post, image=image)

        return post
