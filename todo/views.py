from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    person =[
        {"name":"Nisha","age":"23"},
        {"name":"isha","age":"53"},
        {"name":"miha","age":"13"},
        {"name":"miha","age":"13"},
        {"name":"miha","age":"13"},
        {"name":"miha","age":"13"},
        {"name":"miha","age":"13"}
    ]
    context = {
        "key":"Anisha",
        "persons":person
    }
    return render(request,'index.html',context) 
    # return HttpResponse("First app")

def contact(request):
    return HttpResponse("This is contact page!")

def aboutpage(request):
    return HttpResponse("This is about page!")

def welcome(request):
    return HttpResponse("Welcome to my first Django app!")