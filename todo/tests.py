from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Todo

User = get_user_model()

class TodoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='elena', password='elena33')

    def test_todo_created(self):
        todo_obj = Todo.objects.create(content="my todo", user=self.user)
        self.assertEqual(todo_obj.id, 1)
        self.assertEqual(todo_obj.user, self.user)