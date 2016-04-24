# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0004_auto_20160421_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='difficulty_comment',
            field=models.TextField(max_length=6000, blank=True),
        ),
    ]
