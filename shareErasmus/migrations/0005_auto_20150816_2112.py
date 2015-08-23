# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0004_auto_20150816_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subject',
            field=models.ManyToManyField(to='shareErasmus.Subject', blank=True),
            preserve_default=True,
        ),
    ]
