from django.db import models
from .models import *

class Forum(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Forum_Post(models.Model):
    content=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    forum=models.ForeignKey(Forum, related_name='all_forum_posts', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
