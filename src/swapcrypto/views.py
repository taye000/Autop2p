from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def sign_in(request):
    return HttpResponse('<h1>Welcome back. Please Sign in.</h1>')
