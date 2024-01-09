from django.shortcuts import render,redirect
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
    tasks=Task.objects.get(id=id)
    if req.method=="POST":
        task=req.POST.get('task','')
        priority=req.POST.get('priority','')
        Task.objects.filter(id=id).update(task=task,priority=priority)
        return redirect("home")
    return render(req,'update.html',{"task":tasks})

def Delete(req,id):
    tasks=Task.objects.get(id=id)
    if req.method=="POST":
                                              
        
        Task.objects.filter(id=id).delete()
        return redirect("home")
    return render(req,'delete.html',{"task":tasks})