# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150222_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_publish',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 23, 8, 14, 20, 948505), help_text=' ', verbose_name='Publish Date'),
            preserve_default=True,
        ),
    ]
