# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories', 'ordering': ['title'], 'verbose_name': 'Category'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='Slug', default=datetime.datetime(2015, 2, 12, 7, 46, 25, 982321, tzinfo=utc), help_text='Uri identifier.', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(null=True, verbose_name='Categories', help_text=' ', to='blog.Category', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_publish',
            field=models.DateTimeField(auto_now=True, help_text=' ', verbose_name='Publish Date'),
            preserve_default=True,
        ),
    ]
