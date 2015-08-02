# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='shortName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.AlterField(
            model_name='university',
            name='description',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
    ]
