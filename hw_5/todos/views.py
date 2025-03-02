from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Todo
from .forms import TodoForm

# Страница логина (GET)
def login_view(request):
    return render(request, 'login.html')

# Авторизация (POST)
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/todos/')
        else:
            return render(request, 'login.html', {'error': 'Неверные данные'})
    return redirect('/login/')

# Выход пользователя
def logout_user(request):
    logout(request)
    return redirect('/login/')

# Список задач пользователя
@login_required
def todos_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos.html', {'todos': todos})

# Просмотр конкретной задачи
@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todo_detail.html', {'todo': todo})

# Создание новой задачи
@login_required
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('/todos/')
    else:
        form = TodoForm()
    return render(request, 'create_todo.html', {'form': form})

# Удаление задачи
@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if todo.user != request.user:
        return HttpResponseForbidden()
    todo.delete()
    return redirect('/todos/')
