# Generated by Django 3.2.5 on 2021-08-15 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title_0',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_1',
            new_name='title',
        ),
    ]
