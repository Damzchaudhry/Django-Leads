# Generated by Django 2.0 on 2019-05-22 12:08

import ckeditor.fields
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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Topic')),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(unique='True')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Posted on')),
                ('article_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author ')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='Comment')),
                ('comment_content', models.CharField(max_length=200, verbose_name='Co')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article', verbose_name='Article')),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]
