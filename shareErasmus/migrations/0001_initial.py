# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=3000, blank=True)),
                ('prices', models.CharField(max_length=3000, blank=True)),
                ('weather', models.CharField(max_length=500, blank=True)),
                ('student_life', models.CharField(max_length=4000, blank=True)),
                ('culture', models.CharField(max_length=3000, blank=True)),
                ('lodging', models.CharField(max_length=4000, blank=True)),
                ('nightlife', models.CharField(max_length=3000, blank=True)),
                ('information_interest', models.CharField(max_length=3000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('body', models.CharField(max_length=2000)),
                ('dateTime', models.DateTimeField()),
                ('parent', models.ForeignKey(blank=True, to='shareErasmus.Comment', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('difficulty', models.CharField(blank=True, max_length=1, choices=[(b'5', b'Muy f\xc3\xa1cil'), (b'4', b'f\xc3\xa1cil'), (b'3', b'Normal'), (b'2', b'dif\xc3\xadcil'), (b'1', b'Muy dif\xc3\xadcil')])),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('description', models.CharField(max_length=3000, blank=True)),
                ('validation_subjects', models.CharField(max_length=4000, blank=True)),
                ('contacts', models.CharField(max_length=3000, blank=True)),
                ('city', models.ForeignKey(to='shareErasmus.City')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('is_public_email', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
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
            field=models.ForeignKey(blank=True, to='shareErasmus.Subject', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='university',
            field=models.ForeignKey(blank=True, to='shareErasmus.University', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='shareErasmus.UserProfile'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='shareErasmus.Country'),
        ),
    ]
