from django.db import models
#from profiles.models import Person

class Todo(models.Model):
    title = models.TextField(max_length=50, blank=True,)
    author = models.TextField(max_length=50, blank=True)
    content = models.TextField(max_length=50, blank=True)
    completed = models.BooleanField(default=False)

    #image = models.ImageField(blank=True)
#    borrowed_by = models.ManyToManyField(Person, related_name='person', blank=True)

    def __str__(self):
        return self.title
