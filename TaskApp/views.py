from django.shortcuts import redirect, render
from .models import Task
# Create your views here.

def openIndex(request):
    return render(request,"index.html")

def openTaskForm(request):
    return render(request,"task-form.html")

def saveTask(request):
    task=Task()
    task.title=request.POST['title']
    task.description=request.POST['description']
    task.dateCreated=request.POST['date-created']
    task.deadlineDate=request.POST['deadline-date']
    task.save()
    return redirect('/tasks-list')

def getAllTasks(request):
    tasks=Task.objects.all()
    return render(request,"all-tasks-list.html",{'tasks':tasks})

def markTaskAsCompleted(request,id):
    task=Task.objects.get(id=id)
    task.completionStatus=True
    task.save()
    return redirect('/tasks-list')

def getPendingTasks(request):
    tasks=Task.objects.filter(completionStatus=False)
    pendingTasks=tasks.values()
    return render(request,"pending-tasks-list.html",{'tasks':pendingTasks})
