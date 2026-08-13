from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "movie", "review", "published_date"]
        # DRF uses extra_kwargs and the 'style' key to modify its browsable HTML forms
        extra_kwargs = {
            'movie': {
                'style': {
                    'placeholder': 'Enter the movie title',
                    'base_template': 'input.html',
                }
            },
            'review': {
                'style': {
                    'placeholder': 'Enter your review',
                    'base_template': 'textarea.html',

                }
            }
        }
