from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.conf import settings

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="following")

    class Meta:
        verbose_name_plural="Users"
    
    def __str__(self):
        return f"{self.id}: {self.username}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    post = models.TextField(blank=False)
    like = models.ManyToManyField(User, blank="True", related_name="likes") 
    created = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        verbose_name_plural="Posts"

    def __str__(self):
        return f"{self.id} by {self.user.username} : {self.post} on {self.created}"
