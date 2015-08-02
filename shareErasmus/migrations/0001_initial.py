# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('body', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('dateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('veryGood', models.IntegerField(default=5)),
                ('good', models.IntegerField(default=4)),
                ('regular', models.IntegerField(default=3)),
                ('bad', models.IntegerField(default=2)),
                ('veryBad', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('score', models.ForeignKey(blank=True, to='shareErasmus.Score', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('shortName', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to=b'')),
                ('date', models.DateField()),
                ('subject', models.ManyToManyField(to='shareErasmus.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='university',
            field=models.ForeignKey(to='shareErasmus.University'),
        ),
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.ForeignKey(to='shareErasmus.Subject'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='shareErasmus.User'),
        ),
    ]
