from django.db import models
from django.contrib.auth.models import User
from match.models.image import Image


class UserInfo(models.Model):
    # imageモデルと１対１の関係である
    image = models.OneToOneField
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    self_introduction = models.CharField(max_length=500,null=True)
    sex = models.CharField(max_length=2)
    created_at = models.DateField(auto_now_add=True)
    objects = models.Manager