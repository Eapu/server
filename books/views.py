from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Book

def home_view(request, *args, **kwargs):
    return render(request, 'books/home.html', context={}, status=200)

def book_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    consume by javascript react
    """
    qs = Book.objects.all()
    books_list = [{"id": x.id, "title":x.title} for x in qs]
    data = {
        "isUser":False,
        "response": books_list
    }
    return JsonResponse(data)

def book_detail_view(request, book_id, *args, **kwargs):
    """
    REST API VIEW
    consume by javascript react
    """
    data = {
    "id": book_id,
    }
    status=200
    try:
        obj = Book.objects.get(id=book_id)
        data['title'] = obj.title
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)
