from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.views.generic import View
from erasmus import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from shareErasmus.models import University, Subject, UserProfile
from shareErasmus.serializers import UniversitySerializer
import json
import datetime

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


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
    user.save()
    userProfile = UserProfile(user=user)
    userProfile.save()

#SACAR FUERA DE VIEWS.PY
def authenticateUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(password=password,username=username)
    if user:
        login(request, user)
    else:
        pass


class LoginView(View):
    def get(self, request):
        return render(request, "pages/login.html")

    def post(self, request):
        if 'sign-in' in request.POST:
            registerUser(request)
        elif 'login' in request.POST:
            authenticateUser(request)

        return render(request, "pages/index.html")



class ContactView(View):
    def get(self, request):
        return render(request, "pages/contact.html")

###############
#Profile views#
###############
class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return render(request, "pages/myProfile/indexProfile.html")
        else:
            return render(request, "accessDenied.html")



class UniversityProfileView(View):
    def get(self, request):
        pass
