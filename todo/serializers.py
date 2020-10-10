from django.conf import settings
from rest_framework import serializers
from .models import Todo

MAX_TODO_LENGTH = settings.MAX_TODO_LENGTH
TODO_ACTION_OPTIONS = settings.TODO_ACTION_OPTIONS

class TodoActionSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	action = serializers.CharField()
	content = serializers.CharField(allow_blank=True, required=False)

	def validate_action(self, value):
		value = value.lower().strip()
		if not value in TODO_ACTION_OPTIONS:
			raise serializers.ValidationError("This is not a valid action")
		return value

class TodoCreateSerializer(serializers.ModelSerializer):
	assign = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Todo
		fields = ('id', 'content', 'assign', 'completed')
	def get_assign(self, obj):
		return obj.assign.count()

	def validate_content(self, value):
		if len(value) > MAX_TODO_LENGTH:
			raise serializers.ValidationError("This todo is to long")
		return value


class TodoSerializer(serializers.ModelSerializer):
	assign = serializers.SerializerMethodField(read_only=True)
	content = serializers.SerializerMethodField(read_only=True)
	parent = TodoCreateSerializer(read_only=True)
	class Meta:
		model = Todo
		fields = ('id', 'content', 'assign', 'is_retodo', 'parent', 'completed')

	def get_assign(self, obj):
		return obj.assign.count()

	def get_content(self, obj):
		content = obj.content
		if obj.is_retodo:
			content = obj.parent.content
		return content
