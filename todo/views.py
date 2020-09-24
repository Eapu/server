from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Todo
from .forms import TodoForm

def home_view(request, *args, **kwargs):
    return render(request, 'todo/home.html', context={}, status=200)

def todo_create_view(request, *args, **kwargs):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TodoForm()
    return render(request, 'todo/components/forms.html', context={"form":form})
    
def todo_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    consume by javascript react
    """
    qs = Todo.objects.all()
    todo_list = [{"id": x.id, "title":x.title,"title":x.content} for x in qs]
    data = {
        "isUser":False,
        "response": todo_list
    }
    return JsonResponse(data)

def todo_detail_view(request, todo_id, *args, **kwargs):
    """
    REST API VIEW
    consume by javascript react
    """
    data = {
    "id": todo_id,
    }
    status=200
    try:
        obj = Todo.objects.get(id=todo_id)
        data['title'] = obj.title
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)
