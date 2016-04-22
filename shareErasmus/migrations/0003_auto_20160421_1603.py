# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0002_auto_20160420_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='subjects',
            new_name='subject',
        ),
    ]
