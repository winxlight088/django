from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    person =[
        {"name":"Nisha","age":23},
        {"name":"isha","age":53},
        {"name":"miha","age":13},
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 22},
        {"name": "Diana", "age": 28},
        {"name": "Ethan", "age": 35},
        {"name": "Fiona", "age": 26},
        {"name": "George", "age": 29},
        {"name": "Hannah", "age": 24},
        {"name": "Ian", "age": 31},
        {"name": "Julia", "age": 27}
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