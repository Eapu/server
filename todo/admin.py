from django.contrib import admin
from .models import Todo # add this

class TodoAdmin(admin.ModelAdmin):  # add this
    list_display = ('user', 'content', 'completed') # add this
    search_fieds = ['user__username', 'user_email']
    class Meta:
        model = Todo
# Register your models here.
admin.site.register(Todo, TodoAdmin) # add this