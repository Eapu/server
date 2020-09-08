from django.db import models
#from profiles.models import Person

class Book(models.Model):
    title = models.TextField(max_length=50, blank=True,)
    author = models.TextField(max_length=50, blank=True)
    isbn_number = models.CharField(max_length=50, blank=True)
    category = models.TextField(max_length=50, blank=True)
    description = models.TextField(max_length=200, blank=True)
    loan = models.BooleanField(max_length=20, blank=True,null = True)
    barCode = models.CharField(max_length=20, blank=True)
    language = models.TextField(max_length=20, blank=True)
    image = models.ImageField(blank=True)
#    borrowed_by = models.ManyToManyField(Person, related_name='person', blank=True)

    def __str__(self):
        return self.title
