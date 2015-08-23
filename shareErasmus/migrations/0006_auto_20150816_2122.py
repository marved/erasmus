# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0005_auto_20150816_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subject',
            field=models.ManyToManyField(to='shareErasmus.Subject'),
            preserve_default=True,
        ),
    ]
