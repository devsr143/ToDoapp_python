from django.shortcuts import render, redirect

from new_app.forms import ToDoForm
from new_app.models import ToDo


def index(request):
    return render(request, 'index.html')

def add_todo(request):
    form = ToDoForm()
    if request.method == 'POST':
        form1 = ToDoForm(request.POST)
        if form1.is_valid():
            form1.save()
    return  render(request, 'todo_dash.html', {'form': form})

def get(request):
    data = ToDo.objects.all()
    return  render(request,'dashboard.html',{'data':data})

def delete_data(request,id):
    data = ToDo.objects.get(id = id)
    data.delete()
    return  redirect("/dashboard/")

def update_data(request,id):
    data = ToDo.objects.get(id = id)
    form = ToDoForm(instance=data)
    if request.method == "POST":
        form1 = ToDoForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
        return redirect("/dashboard/")
    return  render(request,"update.html",{"form":form})
