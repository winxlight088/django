from django.shortcuts import render,HttpResponse
from todo.models import Todolist
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
        "p":person
    }
    return render(request,'index.html',context) 
    # return HttpResponse("First app")

def contact(request):
    return render(request,'contact.html')



def todo(request):
    tasks = Todolist.objects.all() #Todolist class is obtained from models.py 
    total_tasks = tasks.count() #cout the number of task
    pending_tasks =tasks.filter(state=False).count()
    complete_tasks= tasks.filter(state=True).count()
    context = {
        "t" : tasks,
        "total_task" : total_tasks,
        "pend_task" : pending_tasks,
        "comp_task" : complete_tasks
    }
    return render(request,'todolist.html',context)