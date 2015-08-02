#encoding:utf-8
from django.db import models

class Link(models.Model):
    url = models.URLField()

class Score(models.Model):
    veryGood = models.IntegerField(default=5)
    good = models.IntegerField(default=4)
    regular = models.IntegerField(default=3)
    bad = models.IntegerField(default=2)
    veryBad = models.IntegerField(default=1)

class University(models.Model):
    name = models.CharField(max_length=150, unique=True)
    shortName = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score = models.ForeignKey(Score, null=True, blank=True)
    university = models.ForeignKey(University)

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    #photo = models.ImageField()
    subject = models.ManyToManyField(Subject)
    date = models.DateField()   #Date of account creation


class Comment(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    body = models.CharField(max_length=300)
    date = models.DateField()
    dateTime = models.DateTimeField()
    subject = models.ForeignKey(Subject)




