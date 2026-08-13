from django.db import models
from django import forms

class BlogPost(models.Model):
    movie = models.CharField(max_length=100)
    review = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie
# Create your models here.
