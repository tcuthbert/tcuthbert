# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150222_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_publish',
            field=models.DateTimeField(default=datetime.date(2015, 2, 22), verbose_name='Publish Date', help_text=' '),
            preserve_default=True,
        ),
    ]
