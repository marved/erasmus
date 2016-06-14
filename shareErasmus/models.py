#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
import datetime
from erasmus import settings

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
    transport = models.CharField(max_length=3000, blank=True)
    mobile_phone = models.CharField(max_length=3000, blank=True)
    bank_account = models.CharField(max_length=3000, blank=True)
    restaurants = models.CharField(max_length=3000, blank=True)
    shopping = models.CharField(max_length=3000, blank=True)
    tourism = models.CharField(max_length=4000, blank=True)

    def __unicode__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=150, unique=True)
    city = models.ForeignKey(City)
    description = models.CharField(max_length=3000, blank=True)
    contacts = models.CharField(max_length=3000, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=150)
    university = models.ForeignKey(University)
    description = models.TextField(max_length=6000, blank=True)
    validation_subjects = models.CharField(max_length=4000, blank=True)
    credits_ects = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class UserProfile(User):
    is_public_email = models.BooleanField(default=False)
    subjects = models.ManyToManyField(Subject, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    body = models.CharField(max_length=2000)
    dateTime = models.DateTimeField(blank=True)
    university = models.ForeignKey(University, blank=True, null=True)
    subject = models.ForeignKey(Subject, blank=True, null=True)
    #parent = models.ForeignKey('self', blank=True, null=True)








