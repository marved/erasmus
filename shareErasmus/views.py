from django.shortcuts import render
from django.views.generic import View
import json


def loadJson(file):
    json_data = open(file)
    data1 = json.load(json_data) # deserialises it
    data2 = json.dumps(json_data) # json formatted string
    json_data.close()
    return data2



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
        return render(request, "pages/myProfile/indexProfile.html" )

class UniversityProfileView(View):
    def get(self, request):
        
        return render(request, "pages/myProfile/universityProfile.html" )
