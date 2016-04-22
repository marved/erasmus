#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

VERY_HARD = '1'
HARD = '2'
REGULAR = '3'
EASY = '4'
VERY_EASY = '5'
hardness_choices = (
         (VERY_EASY,'Muy fácil'),
         (EASY,'fácil'),
         (REGULAR,'Normal'),
         (HARD,'difícil'),
         (VERY_HARD,'Muy difícil')

)

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country)
    description = models.CharField(max_length=3000, blank=True)
    prices = models.CharField(max_length=3000, blank=True)
    weather = models.CharField(max_length=500, blank=True)
    student_life = models.CharField(max_length=4000, blank=True)
    culture = models.CharField(max_length=3000, blank=True)
    lodging = models.CharField(max_length=4000, blank=True)
    nightlife = models.CharField(max_length=3000, blank=True)
    information_interest = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=150, unique=True)
    city = models.ForeignKey(City)
    description = models.CharField(max_length=3000, blank=True)
    validation_subjects = models.CharField(max_length=4000, blank=True)
    contacts = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=150)
    difficulty = models.CharField(max_length=1, choices=hardness_choices, blank=True)
    university = models.ForeignKey(University)

    def __unicode__(self):
        return self.name

class UserProfile(User):
    photo = models.ImageField(blank=True, null=True)
    is_public_email = models.BooleanField(default=False)
    subjects = models.ManyToManyField(Subject, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=80)
    body = models.CharField(max_length=2000)
    dateTime = models.DateTimeField()
    university = models.ForeignKey(University, blank=True, null=True)
    subject = models.ForeignKey(Subject, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)








