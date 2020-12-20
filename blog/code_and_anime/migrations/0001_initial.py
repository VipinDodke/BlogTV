# Generated by Django 3.1.4 on 2020-12-19 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contect',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(default='', max_length=50)),
                ('Call', models.IntegerField()),
                ('desc', models.CharField(max_length=1100)),
            ],
        ),
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(default='', max_length=200)),
                ('desc', models.CharField(default='', max_length=700)),
                ('desc1', models.CharField(default='', max_length=700)),
                ('post_date', models.DateField()),
                ('TypeBlog', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='blog/images')),
                ('video', models.FileField(default='', upload_to='blog/video')),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='code_and_anime.page')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
