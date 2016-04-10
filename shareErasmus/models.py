#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

VERY_BAD = '1'
BAD = '2'
REGULAR = '3'
GOOD = '4'
VERY_GOOD = '5'
scores_choices = (
         (VERY_GOOD,'Muy bien'),
         (GOOD,'Bien'),
         (REGULAR,'Regular'),
         (BAD,'Mal'),
         (VERY_BAD,'Muy mal')

)


class UserProfile(User):
    photo = models.ImageField(blank=True, null=True)

class University(models.Model):
    name = models.CharField(max_length=150, unique=True)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    description = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score = models.CharField(max_length=1, choices=scores_choices)
    university = models.ForeignKey(University)
    users = models.ManyToManyField(UserProfile, blank=True)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=80)
    body = models.CharField(max_length=300)
    dateTime = models.DateTimeField()
    university = models.ForeignKey(University)
    subject = models.ForeignKey(Subject)







