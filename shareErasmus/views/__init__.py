from django.shortcuts import redirect, render
from django.contrib.auth import logout


def do_logout(request):
    logout(request)
    return redirect('/')


def not_found(request):
        return render(request, '404.html')
