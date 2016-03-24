# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('body', models.CharField(max_length=300)),
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
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('score', models.CharField(max_length=1, choices=[(b'1', b'Very Bad'), (b'2', b'Bad'), (b'3', b'Regular'), (b'4', b'Good'), (b'5', b'Very Good')])),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=1000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='university',
            field=models.ForeignKey(to='shareErasmus.University'),
        ),
        migrations.AddField(
            model_name='subject',
            name='users',
            field=models.ManyToManyField(to='shareErasmus.UserProfile', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.ForeignKey(to='shareErasmus.Subject'),
        ),
        migrations.AddField(
            model_name='comment',
            name='university',
            field=models.ForeignKey(to='shareErasmus.University'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='shareErasmus.UserProfile'),
        ),
    ]
