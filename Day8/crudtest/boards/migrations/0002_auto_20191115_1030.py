# Generated by Django 2.2.7 on 2019-11-15 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boards',
            old_name='creatot',
            new_name='creator',
        ),
    ]
