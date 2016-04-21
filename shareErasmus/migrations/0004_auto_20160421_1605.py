# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0003_auto_20160421_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='subject',
            new_name='subjects',
        ),
    ]
