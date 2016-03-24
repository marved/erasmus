from django.contrib import admin

from models import Link
from models import UserProfile
from models import University
from models import Subject
from models import Comment

admin.site.register(Link)
admin.site.register(UserProfile)
admin.site.register(University)
admin.site.register(Subject)
admin.site.register(Comment)
