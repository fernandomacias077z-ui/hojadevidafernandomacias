from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# --- VISTAS PÚBLICAS ---
def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        try:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password"],
            )
            user.save()
            login(request, user)
            return redirect('tasks')
        except IntegrityError:
            return render(request, "signup.html", {"form": UserCreationForm, "error": "El usuario ya existe."})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error':'Usuario o contraseña incorrectos.'})
        else:
            login(request, user)
            return redirect('tasks')

def signout(request):
    logout(request)
    return redirect('home')

# --- VISTAS PRIVADAS (Requieren Login) ---

@login_required
def profile_cv(request):
    # Carga tu hoja de vida de experto en hardware
    return render(request, 'profile_cv.html')

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {'tasks': tasks, 'tipopagina': 'Tareas Pendientes'})

@login_required
def tasks_completed(request):
    # Esta función resuelve el Server Error (500)
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {'tasks': tasks, 'tipopagina': 'Tareas Completadas'})

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, "create_task.html", {'form': TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, "create_task.html", {'form': TaskForm, 'error': 'Datos inválidos.'})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error al actualizar.'})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user) 
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user) 
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')