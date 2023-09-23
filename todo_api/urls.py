# todo/todo_api/urls.py : API urls.py
# from django.conf.urls import url
from django.urls import path, include
from .views.todo import (
    TodoView, 
    TodoListView
)

urlpatterns = [
    path('todos', TodoListView.as_view()),
    path('todos/<int:todo_id>/', TodoView.as_view()),
]

