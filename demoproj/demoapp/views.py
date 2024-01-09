from django.shortcuts import render
# from django.http import HttpResponse
from .models import Task

# Create your views here.
def home(req):
    if req.method=="POST":
        task=req.POST.get('task','')
        priority=req.POST.get('priority','')
        todo=Task(task=task,priority=priority)
        todo.save() 
    tasks=Task.objects.all()
    return render(req,'index.html',{"tasks":tasks})
def Update(req,id):
    task=Task.objects.get(id=id)
    return render(req,'update.html',{"task":task})