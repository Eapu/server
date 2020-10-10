from django.conf import settings
from django import forms
from .models import Todo

MAX_TODO_LENGTH = settings.MAX_TODO_LENGTH

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TODO_LENGTH:
            raise forms.ValidationError("This todo is too long")
        return content