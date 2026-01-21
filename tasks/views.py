from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Task, Experience
from .forms import TaskForm # Debes crear un forms.py simple

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_cv')
    return render(request, 'signup.html', {'form': UserCreationForm()})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile_cv')
    return render(request, 'signin.html', {'form': AuthenticationForm()})

@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def profile_cv(request):
    experiences = Experience.objects.filter(user=request.user)
    return render(request, 'profile_cv.html', {'experiences': experiences})

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()
        return redirect('tasks')
    return render(request, 'create_task.html', {'form': TaskForm()})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    return render(request, 'task_detail.html', {'task': task})