from django.contrib import admin
from django.urls import path, re_path
from todo.views import (
    home_view,todo_list_view, todo_detail_view,
    todo_create_view,
)

urlpatterns = [
    path('', home_view),
    path('todo/',todo_list_view),
    path('create-todo/',todo_create_view),
    path('todo/<int:todok_id>',todo_detail_view),


]

