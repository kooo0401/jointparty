from django.db import models
from django.contrib.auth.models import User
from match.models.image import Image

# Create your models here.
class UserInfo(models.Model):
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    self_introduction = models.CharField(max_length=500,null=True)
    sex = models.CharField(max_length=5)
    created_at = models.DateField(auto_now_add=True)
    objects = models.Manager