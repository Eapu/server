from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from todo.views import (
    home_view,todo_list_view,
    todo_action_view,
    todo_detail_view,
    todo_delete_view, todo_create_view,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('react/', TemplateView.as_view(template_name='todo/react.html')),
    path('todo',todo_list_view),
    path('create-todo',todo_create_view),
    path('todo/<int:todo_id>',todo_detail_view),
    path('api/todo/',include('todo.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                document_root=settings.STATIC_ROOT)
