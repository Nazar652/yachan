# Generated by Django 4.2.3 on 2023-07-25 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_threadmodel_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['time_created']},
        ),
        migrations.AlterModelOptions(
            name='threadmodel',
            options={'ordering': ['last_post']},
        ),
        migrations.AddField(
            model_name='threadmodel',
            name='last_post',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
