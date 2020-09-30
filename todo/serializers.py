from django.conf import settings
from rest_framework import serializers
from .models import Todo

MAX_TODO_LENGTH = settings.MAX_TODO_LENGTH

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'content', 'completed')

    def validate_content(self,value):
        if len(value) > MAX_TODO_LENGTH:
          raise serializers.ValidationError("This todo is too long")
        return value