from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        return render(request, "pages/index.html" )


class LoginView(View):
    def get(self, request):
        return render(request, "pages/login.html" )


class ContactView(View):
    def get(self, request):
        return render(request, "pages/contact.html" )
