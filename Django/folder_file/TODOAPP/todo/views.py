from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Task
# Create your views here.


def show_task(request):
    task =  Task.objects.all().order_by('-createdAt')
    return render(request,'todo/show_task.html',{'task':task})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title','').strip()
        description = request.POST.get('description','').strip()

        if title:
            Task.objects.create(title=title,description=description)
            return redirect(reverse('show_task'))

        return render(request,'todo/task_form.html',{'error':'Title cannot be empty'})

    return render(request,'todo/task_form.html')  


def edit_task(request,tk):
    task = get_object_or_404(Task,id=tk)
    if request.method == 'POST':
        title = request.POST.get('title','').strip()
        description = request.POST.get('description','').strip()
        completed = request.POST.get('completed')=='on'

        if title:
            task.title = title
            task.description = description
            task.completed = completed
            task.save()

            return redirect(reverse('show_task'))
    return render(request,'todo/task_form.html',{'task':task})


def delete_task(request,tk):
    task = get_object_or_404(Task,id=tk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('show_task'))  
    return render(request,'todo/task_confirm_delete.html',{'task':task})      


def toggle_task(request,tk):
    task = get_object_or_404(Task,id=tk)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect(reverse('show_task'))
