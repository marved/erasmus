# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareErasmus', '0005_subject_difficulty_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='bank_account',
            field=models.CharField(max_length=3000, blank=True),
        ),
        migrations.AddField(
            model_name='city',
            name='mobile_phone',
            field=models.CharField(max_length=3000, blank=True),
        ),
        migrations.AddField(
            model_name='city',
            name='restaurants',
            field=models.CharField(max_length=3000, blank=True),
        ),
        migrations.AddField(
            model_name='city',
            name='shopping',
            field=models.CharField(max_length=3000, blank=True),
        ),
        migrations.AddField(
            model_name='city',
            name='tourism',
            field=models.CharField(max_length=4000, blank=True),
        ),
        migrations.AddField(
            model_name='city',
            name='transport',
            field=models.CharField(max_length=3000, blank=True),
        ),
    ]
