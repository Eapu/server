from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

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