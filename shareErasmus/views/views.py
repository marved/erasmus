from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        return render(request, "pages/index.html")


class SignView(View):
    def get(self, request):
        return render(request, "pages/sign.html")



class UniversitiesView(View):
    def get(self, request):
        return render(request, "pages/universities.html")


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



