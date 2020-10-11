from django.contrib import admin
from django.urls import path
from todo.views import (
    home_view,todo_list_view,
    todo_action_view,
    todo_detail_view,
    todo_delete_view, todo_create_view,
)
app_name = 'todo'
urlpatterns = [
    path('',todo_list_view),
    path('create/',todo_create_view),
    path('<int:todo_id>/',todo_detail_view),
    path('action/',todo_action_view),
    path('<int:todo_id>/delete/',todo_delete_view),


]

