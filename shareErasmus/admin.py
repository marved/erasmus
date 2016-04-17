from django.contrib import admin

from models import Country
from models import City
from models import UserProfile
from models import University
from models import Subject
from models import Comment

admin.site.register(Country)
admin.site.register(City)
admin.site.register(UserProfile)
admin.site.register(University)
admin.site.register(Subject)
admin.site.register(Comment)
