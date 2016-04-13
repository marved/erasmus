from django.shortcuts import render
from django.views.generic import View
from shareErasmus.models import University


class HomeView(View):
    def get(self, request):
        return render(request, "pages/index.html")


class SignView(View):
    def get(self, request):
        return render(request, "pages/sign.html")



class UniversitiesView(View):
    def get(self, request):
        universities = University.objects.all().order_by('name')
        context = {
            'universities': universities
        }
        return render(request, "pages/universities.html", context)


class ContactView(View):
    def get(self, request):
        return render(request, "pages/contact.html")

###############
#Settings views#
###############
class AccountView(View):
    def get(self, request):
  #      if request.user.is_authenticated():
            return render(request, "pages/settings/account.html")
 #       else:
 #           return render(request, "accessDenied.html")


class MyUniversitiesView(View):
    def get(self, request):
        return render(request, "pages/settings/myUniversities.html")



