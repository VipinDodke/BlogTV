# Generated by Django 3.1.4 on 2020-12-19 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_and_anime', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contect',
            name='desc',
        ),
    ]
