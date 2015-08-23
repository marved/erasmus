from django.shortcuts import render
from django.views.generic import View
from erasmus import settings
from shareErasmus.models import Country, University, Subject
import json


def loadJson(file):
    json_data = open(file)
    data1 = json.load(json_data) # deserialises it
    data2 = json.dumps(json_data) # json formatted string
    json_data.close()
    return data1



class HomeView(View):
    def get(self, request):
        return render(request, "pages/index.html" )


class ContactView(View):
    def get(self, request):
        return render(request, "pages/contact.html" )

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
        return render(request, "pages/myProfile/universityProfile.html", ctx )
