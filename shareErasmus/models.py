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

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country)
    description = models.CharField(max_length=1000, blank=True)
    prices = models.CharField(max_length=500, blank=True)
    weather = models.CharField(max_length=500, blank=True)
    student_life = models.CharField(max_length=1000, blank=True)
    culture = models.CharField(max_length=1000, blank=True)
    lodging = models.CharField(max_length=1000, blank=True)
    nightlife = models.CharField(max_length=1000, blank=True)
    information_interest = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.name

class UserProfile(User):
    photo = models.ImageField(blank=True, null=True)

class University(models.Model):
    name = models.CharField(max_length=150, unique=True)
    city = models.ForeignKey(City)
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







