# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20150307_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_publish',
            field=models.DateTimeField(verbose_name='Publish Date', help_text=' ', default=datetime.datetime(2015, 3, 7, 14, 8, 49, 400692)),
            preserve_default=True,
        ),
    ]
