from django.db import models
from match.models.userinfo import UserInfo
from django.utils import timezone

class Posts(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    number = models.IntegerField(null=False)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    venue = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    objects = models.Manager