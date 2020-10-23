from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Todo
from .forms import TodoForm
from .serializers import (
    TodoSerializer,
    TodoActionSerializer,
    TodoCreateSerializer)

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

@permission_classes([IsAuthenticated])
def home_view(request, *args, **kwargs):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'todo/home.html', context={"username":username}, status=200)

@api_view(['POST']) # http method the client == POST
#@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def todo_create_view(request, *args, **kwargs):
    serializer = TodoCreateSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def todo_detail_view(request, todo_id, *args, **kwargs):
    qs = Todo.objects.filter(id=todo_id)
    if not qs.exists():
        return Response({},status=404)
    obj = qs.first()
    serializer = TodoSerializer(obj)
    return Response(serializer.data, status=200)

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def todo_action_view(request, *args, **kwargs):
    # id required
    print(request.POST, request.data)
    serializer = TodoActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        todo_id = data.get("id")
        action = data.get("action")
        content = data.get("content")
        qs = Todo.objects.filter(id=todo_id)
        if not qs.exists():
            return Response({},status=404)
        obj = qs.first()
        if action == "assign":
            obj.assign.add(request.user)
            serializer = TodoSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "unassign":
            obj.assign.remove(request.user)
            serializer = TodoSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "retodo":
            new_todo = Todo.objects.create(
                user=request.user,
                parent=obj,
                content=content,
                )
            serializer = TodoSerializer(new_todo)
            return Response(serializer.data, status=201)
    return Response({}, status=200)

@api_view(['GET','DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def todo_delete_view(request, todo_id, *args, **kwargs):
    qs = Todo.objects.filter(id=todo_id)
    if not qs.exists():
        return Response({},status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message": "You cannot delete this"}, status=200)
    obj = qs.first()
    obj.delete()
    return Response({"message":"remove_view"}, status=200)

@api_view(['GET'])
def todo_list_view(request, *args, **kwargs):
    qs = Todo.objects.all()
    serializer = TodoSerializer(qs, many=True)
    return Response(serializer.data)

def todo_create_view_dj(request, *args, **kwargs):

    # REST API CREATE VIEW ->DRF

    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    form = TodoForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201) #201 ==created items
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TodoForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'todo/components/form.html', context={"form":form})

def todo_list_view_dj(request, *args, **kwargs):
    """
    REST API VIEW
    consume by javascript react
    """
    qs = Todo.objects.all()
    todo_list = [x.serialize() for x in qs]
    data = {
        "isUser":False,
        "response": todo_list
    }
    return JsonResponse(data)

def todo_detail_view_dj(request, todo_id, *args, **kwargs):
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
