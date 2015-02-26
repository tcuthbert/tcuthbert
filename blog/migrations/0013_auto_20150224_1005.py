# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150223_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_publish',
            field=models.DateTimeField(verbose_name='Publish Date', default=datetime.datetime(2015, 2, 24, 10, 5, 17, 425914), help_text=' '),
            preserve_default=True,
        ),
    ]
