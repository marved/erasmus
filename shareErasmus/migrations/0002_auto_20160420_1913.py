# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='users',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subjects',
            field=models.ManyToManyField(to='shareErasmus.Subject', blank=True),
        ),
    ]
