from django.shortcuts import render
from django.views.generic import View
from erasmus import settings
from django.contrib.auth.models import User
from shareErasmus.models import Country, University, Subject, UserProfile
import json
import datetime


def loadJson(file):
    json_data = open(file)
    data1 = json.load(json_data) # deserialises it
    data2 = json.dumps(json_data) # json formatted string
    json_data.close()
    return data1



class HomeView(View):
    def get(self, request):
        return render(request, "pages/index.html")


#SACAR FUERA DE VIEWS.PY
def registerUser(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username,email,password)
    user.last_login=user.last_joined
    user.save()
    userProfile = UserProfile(user=user)
    userProfile.save()


class LoginView(View):
    def get(self, request):
        return render(request, "pages/login.html")

    def post(self, request):
        if 'sign-in' in request.POST:
            registerUser(request)

        return render(request, "pages/index.html")



class ContactView(View):
    def get(self, request):
        return render(request, "pages/contact.html")

###############
#Profile views#
###############
class ProfileView(View):
    def get(self, request):
        return render(request, "pages/myProfile/indexProfile.html")

class UniversityProfileView(View):
    def get(self, request):
        countries = Country.objects.all()
        universities = University.objects.all()
        subjects = Subject.objects.all()
        ctx = {'countries': countries,
               'universities': universities,
               'subjects': subjects}
        return render(request, "pages/myProfile/universityProfile.html", ctx)
