# Generated by Django 4.2.3 on 2023-07-22 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_imagemodel_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='threadmodel',
            options={'ordering': ['-id']},
        ),
    ]