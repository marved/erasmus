#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    url = models.URLField()

class Score(models.Model):
    veryGood = models.IntegerField(default=5)
    good = models.IntegerField(default=4)
    regular = models.IntegerField(default=3)
    bad = models.IntegerField(default=2)
    veryBad = models.IntegerField(default=1)

class Country(models.Model):
    name = models.CharField(max_length=150, unique=True)

class University(models.Model):
    name = models.CharField(max_length=150, unique=True)
    country = models.ForeignKey(Country)
    description = models.CharField(max_length=1000, blank=True)

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score = models.ForeignKey(Score, null=True, blank=True)
    university = models.ForeignKey(University)

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    #photo = models.ImageField()
    subject = models.ManyToManyField(Subject, blank=True)


class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=80)
    body = models.CharField(max_length=300)
    date = models.DateField()
    dateTime = models.DateTimeField()
    subject = models.ForeignKey(Subject)




