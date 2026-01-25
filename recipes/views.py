from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return HttpResponse('home')
    return render(request, 'home.html')


def sobre(request):
    return HttpResponse('sobre')


def contato(request):
    return HttpResponse('contato')
    # return http response
