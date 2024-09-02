from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    img = models.ImageField(upload_to="posts/", null=True , blank=True)
    active = models.BooleanField(default=False)
  
    def __str__(self):
        return self.title 