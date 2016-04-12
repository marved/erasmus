from django.shortcuts import redirect
from django.contrib.auth import logout


def do_logout(request):
    logout(request)
    return redirect('/')
