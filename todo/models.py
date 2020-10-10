from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Todo(models.Model):
    # id = models.AutoField(primary_key=True)
    parent = models.ForeignKey("self",  blank=True, null=True, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True)
    assign = models.ManyToManyField(User, related_name='todo_user', blank=True, through='TodoAssign')
    content = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

        # def __str__(self):
    #    return self.content
    class Meta:
        ordering = ['-id']
    #image = models.ImageField(blank=True)
#    borrowed_by = models.ManyToManyField(Person, related_name='person', blank=True)


    @property
    def is_retodo(self):
        return self.parent != None

class TodoAssign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assign = models.ForeignKey(Todo, blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

