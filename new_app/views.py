from django.shortcuts import render

from new_app.forms import ToDoForm


def index(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request, 'dashboard.html')

def new(request):
    return render(request, 'new.html')

def fresh(request):
    return render(request, 'fresh.html')

def add_todo(request):
    form = ToDoForm()
    if request.method == 'POST':
        form1 = ToDoForm(request.POST)
        if form1.is_valid():
            form1.save()
    return  render(request, 'todo_dash.html', {'form': form})