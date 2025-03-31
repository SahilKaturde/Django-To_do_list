from django.shortcuts import render,redirect,get_object_or_404
from .models import Task,Completed_task
from django.views.decorators.http import require_POST



# Create your views here.

def home(request):
    tasks = Task.objects.all()
    return render(request,'home.html',{'tasks':tasks})

def customise(request):
    return render(request,'add.html')

def graph(request):
    return render(request,'graph.html')


"""
YAY !,
    Code for backend handeling 

"""

def add_task (request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_descr = request.POST.get('task_descr')

        

        Task.objects.create(
            task_name = task_name,
            task_descr = task_descr
        )
        print(f"Task Name: {task_name}, Task Description: {task_descr}")
        return redirect('add')
    return render(request , 'add.html')


@require_POST
def delete_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    
    Completed_task.objects.create(
        task_name = task.task_name,
        task_descr = task.task_descr,
    )

    task.delete()
    return redirect('home')


"""
    For Plot
"""
import matplotlib.pyplot as plt
import io
import urllib
import base64


        


