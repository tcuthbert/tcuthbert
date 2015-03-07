# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20150224_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_publish',
            field=models.DateTimeField(help_text=' ', verbose_name='Publish Date', default=datetime.datetime(2015, 3, 7, 14, 7, 17, 807438)),
            preserve_default=True,
        ),
    ]
