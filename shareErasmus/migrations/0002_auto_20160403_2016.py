# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='score',
            field=models.CharField(max_length=1, choices=[(b'5', b'Muy bien'), (b'4', b'Bien'), (b'3', b'Regular'), (b'2', b'Mal'), (b'1', b'Muy mal')]),
        ),
    ]
