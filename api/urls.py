from django.urls import path
from .views import apiOverview, todoList
from . import views

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('task-list/', todoList, name="List"),
    path('task-detail/<str:pk>/', views.todoDetail, name="Task-detail"),
    path('task-create/', views.todoCreate, name='Task-create'),
    path('task-update/<str:pk>/', views.todoUpdate, name='Task-update'),
    path('task-delete/<str:pk>/', views.todoDelete, name='Task-delete'),
]
