# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150222_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_publish',
            field=models.DateTimeField(help_text=' ', verbose_name='Publish Date'),
            preserve_default=True,
        ),
    ]
