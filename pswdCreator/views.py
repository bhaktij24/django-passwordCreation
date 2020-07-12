from django.shortcuts import render
from django.http import HttpResponse
import random as rd
import string
# Create your views here.
def homePage(request):
    #return HttpResponse("Hello there friend!")
    #return render(request,'pswdCreator/home.html',{'password' : 'sdfVE235dshtAS'})
    return render(request,'pswdCreator/home.html')

def passwordPage(request):
    #return HttpResponse("<h1>Welcome to my page</h1>")
    #return render(request,'pswdCreator/password.html')
    characters = list(string.ascii_lowercase)
    thePassword = ''
    #length = 10
    length = int(request.GET.get("length"))
    if request.GET.get("uppercase"):
        characters.extend(string.ascii_uppercase)
    if request.GET.get("spclchar"):
        characters.extend(string.punctuation)
    if request.GET.get("numbers"):
        characters.extend(string.digits)
    for char in range(length):
        thePassword += rd.choice(characters)
    return render(request,"pswdCreator/password.html",{"password": thePassword})

def aboutPage(request):
    return render(request,'pswdCreator/about.html')