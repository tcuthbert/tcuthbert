# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(help_text=' ', verbose_name='Title', max_length=255)),
                ('slug', models.SlugField(verbose_name='Slug', help_text='Uri identifier.', unique=True, max_length=255)),
                ('content_markdown', models.TextField(verbose_name='Content (Markdown)')),
                ('content_markup', models.TextField(help_text=' ', verbose_name='Content (Markup)')),
                ('date_publish', models.DateTimeField(help_text=' ', verbose_name='Publish Date')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'verbose_name': 'Post',
                'ordering': ['-date_publish'],
            },
            bases=(models.Model,),
        ),
    ]
