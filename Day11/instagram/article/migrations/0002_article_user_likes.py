# Generated by Django 2.2.7 on 2019-11-28 13:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user_likes',
            field=models.ManyToManyField(related_name='article_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
