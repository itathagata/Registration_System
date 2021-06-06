from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
# Create your views here.
context = {'welcome':"Welcome to Todo List Page.",
    'contact_text':"Welcome to Todo List Contact Page.",
    'about_text':"Welcome to Todo List About Page."}
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Student Added!"))
        return redirect('todolist')        
    else:
        all_tasks = TaskList.objects.all
        return render(request, 'todolist.html',{'all_tasks':all_tasks})
def complete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.Attendance = True
    task.save()
    return redirect('todolist')

def delete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')




def edit_task(request,task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Edited!"))
        return redirect('todolist')        
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html',{'task_obj':task_obj})


def contact(request):
    return render(request, 'contact.html',context)
def about(request):
    return render(request, 'about.html',context)