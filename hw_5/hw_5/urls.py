from django.contrib import admin
from django.urls import path
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout'),
    path('todos/', views.todos_list, name='todos_list'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/new/', views.create_todo, name='create_todo'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
]
