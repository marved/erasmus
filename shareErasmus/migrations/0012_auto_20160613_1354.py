# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0011_remove_comment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='dateTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
