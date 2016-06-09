# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0008_auto_20160516_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='difficulty_comment',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='difficulty',
        ),
        migrations.AddField(
            model_name='subject',
            name='validation_subjects',
            field=models.CharField(max_length=4000, blank=True),
        ),
    ]
