from rest_framework import serializers 
from .models import BlogPost
from django import forms

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Enter the movie title',
            }),
            'content': forms.EmailInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Enter your movie review',
            }),
        }