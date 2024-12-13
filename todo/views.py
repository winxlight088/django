from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("First app")

def contact(request):
    return HttpResponse("This is contact page!")

def aboutpage(request):
    return HttpResponse("This is about page!")

def welcome(request):
    return HttpResponse("Welcome to my first Django app!")