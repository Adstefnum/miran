# Generated by Django 3.2 on 2021-04-27 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='title',
            new_name='name',
        ),
    ]
