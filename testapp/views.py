from django.shortcuts import render,redirect
from django.http import HttpResponse
from testapp.models import Task


def home(request):
    tasks=Task.objects.filter(is_completed=False) 
    completed_tasks=Task.objects.filter(is_completed=True)# it filters all the tasks which are not completed
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks
    }

    return render(request,'testapp/home.html',context)

def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect(home)

# Create your views here.
