from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from .models import Todo
# Create your tests here.
User = get_user_model()

class TodoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='elena', password='elena33')
        self.userb = User.objects.create_user(username='elena-2', password='elena22')
        Todo.objects.create(content="my first todo", 
            user=self.user)
        Todo.objects.create(content="my first todo", 
            user=self.user)
        Todo.objects.create(content="my first todo", 
            user=self.userb)
        self.currentCount = Todo.objects.all().count()

    def test_todo_created(self):
        todo_obj = Todo.objects.create(content="my second todo", 
            user=self.user)
        self.assertEqual(todo_obj.id, 4)
        self.assertEqual(todo_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_todo_list(self):
        client = self.get_client()
        response = client.get("/api/todo/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    #def test_todo_list(self):
        #client = self.get_client()
        #response = client.get("/api/todo/")
        #self.assertEqual(response.status_code, 403)
        #self.assertEqual(len(response.json()), 3)

    def test_todo_related_name(self):
        user = self.user
        self.assertEqual(user.todo.count(), 2)

    def test_action_assign(self):
        client = self.get_client()
        response = client.post("/api/todo/action/", 
            {"id": 1, "action": "assign"})
        assign_count = response.json().get("assign")
        user = self.user
        my_assign_instances_count = user.todoassign_set.count()
        my_related_assign = user.todo_user.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(like_count, 1)
        self.assertEqual(my_assign_instances_count, 1)
        self.assertEqual(my_assign_instances_count, my_related_assign)
    
    def test_action_unassign(self):
        client = self.get_client()
        response = client.post("/api/todo/action/", 
            {"id": 2, "action": "assign"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/todo/action/", 
            {"id": 2, "action": "unassign"})
        self.assertEqual(response.status_code, 200)
        assign_count = response.json().get("assign")
        self.assertEqual(assign_count, 0)
    
    def test_action_retodo(self):
        client = self.get_client()
        response = client.post("/api/todo/action/", 
            {"id": 2, "action": "retodo"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_todo_id = data.get("id")
        self.assertNotEqual(2, new_todo_id)
        self.assertEqual(self.currentCount + 1, new_todo_id)

    def test_todo_create_api_view(self):
        request_data = {"content": "This is my test todo"}
        client = self.get_client()
        response = client.post("/api/todo/create/", request_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_todo_id = response_data.get("id")
        self.assertEqual(self.currentCount + 1, new_todo_id)
    
    def test_todo_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/todo/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id, 1)

    def test_todo_delete_api_view(self):
        client = self.get_client()
        response = client.delete("/api/todo/1/delete/")
        self.assertEqual(response.status_code, 200)
        client = self.get_client()
        response = client.delete("/api/todo/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete("/api/todo/3/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)
