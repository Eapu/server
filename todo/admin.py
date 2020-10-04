from django.contrib import admin
from .models import Todo, TodoAssign

class TodoAssignAdmin(admin.TabularInline):
    model = TodoAssign


class TodoAdmin(admin.ModelAdmin):
    inlines = [TodoAssignAdmin]
    list_display = ('__str__','user', 'content', 'completed') # add this
    search_fieds = ['user__username', 'user_email']
    class Meta:
        model = Todo
# Register your models here.
admin.site.register(Todo, TodoAdmin) # add this