from http import HTTPStatus
from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request,'home.html')

def password(request):
    character=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get("uppercase"):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get("numbers"):
        character.extend(list('0123456789'))

    if request.GET.get("specialCharacter"):
        character.extend(list('!@#$%^&*()'))
    thepassword=""

    length=int(request.GET.get('length'))
    for i in range(length):
        thepassword+=random.choice(character)

    return render(request,'password.html',{'password':thepassword})

def about(request):
    return render(request,'about.html')

