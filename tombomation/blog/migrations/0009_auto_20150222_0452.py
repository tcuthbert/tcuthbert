# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150222_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_publish',
            field=models.DateTimeField(help_text=' ', verbose_name='Publish Date', default=datetime.datetime(2015, 2, 22, 4, 52, 48, 832099)),
            preserve_default=True,
        ),
    ]
