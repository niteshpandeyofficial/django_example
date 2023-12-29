from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    data={
        "title":'My Websites',
        "data":"Hello Dosto Kaise ho aap log"
    }
    return render(request,"index.html",data)

def contactUs(request):
    return HttpResponse("Welcome to our demo of Django")
def blog(request):
    return HttpResponse("Welcome to our blog page")

def courses(request):
    return HttpResponse("Welcome to our different cources")

def coursesDetails(request,courseid):
    return HttpResponse(courseid)

