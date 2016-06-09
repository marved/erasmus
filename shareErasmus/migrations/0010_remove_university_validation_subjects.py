# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0009_auto_20160609_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='validation_subjects',
        ),
    ]
