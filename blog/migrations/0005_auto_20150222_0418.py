# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150221_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_publish',
            field=models.DateTimeField(default=datetime.date(2015, 2, 22), verbose_name='Publish Date', help_text=' '),
            preserve_default=True,
        ),
    ]
