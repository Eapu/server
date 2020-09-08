from django.contrib import admin
from django.urls import path, re_path
from books.views import home_view, book_detail_view,book_list_view

urlpatterns = [
    path('', home_view),
    path('books/',book_list_view),
    path('books/<int:book_id>',book_detail_view),


]