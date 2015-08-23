# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0006_auto_20150816_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date',
        ),
    ]
