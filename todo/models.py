from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True)
    assign = models.ManyToManyField(User, related_name='todo_user', blank=True, through='TodoAssign')
    content = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
    #image = models.ImageField(blank=True)
#    borrowed_by = models.ManyToManyField(Person, related_name='person', blank=True)

    def __str__(self):
        return self.content

    def serialize(self):
        return {
            "id":self.id,
            "title": self.title,
            "content":self.content
        }

class TodoAssign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
