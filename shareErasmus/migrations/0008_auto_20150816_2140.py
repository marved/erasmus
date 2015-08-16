# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0007_remove_userprofile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subject',
            field=models.ManyToManyField(to='shareErasmus.Subject', blank=True),
            preserve_default=True,
        ),
    ]
