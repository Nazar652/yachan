# Generated by Django 4.2.6 on 2024-04-24 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(max_length=10, unique=True, verbose_name='URL')),
                ('nsfw', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ThreadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=2000)),
                ('updated_text', models.CharField(default=None, max_length=2000, null=True)),
                ('author', models.CharField()),
                ('author_name', models.CharField(default=None, max_length=255, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('last_post', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category', to_field='slug')),
            ],
            options={
                'ordering': ['-last_post'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default=None, max_length=255, null=True)),
                ('text', models.CharField(max_length=2000)),
                ('updated_text', models.CharField(default=None, max_length=2000, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_updated', models.DateTimeField(auto_now=True)),
                ('author', models.CharField()),
                ('author_name', models.CharField(default=None, max_length=255, null=True)),
                ('is_op', models.BooleanField(default=False)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.threadmodel')),
            ],
            options={
                'ordering': ['-time_created'],
            },
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/')),
                ('post', models.ForeignKey(blank=True, limit_choices_to={'thread': None}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.post')),
                ('thread', models.ForeignKey(blank=True, limit_choices_to={'post': None}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.threadmodel')),
            ],
        ),
    ]
