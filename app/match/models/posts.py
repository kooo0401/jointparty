from django.db import models
from match.models.userinfo import UserInfo
from django.utils import timezone

class Posts(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    number = models.IntegerField(max_length=2)
    # date = models.DateField
    # time = models.TimeField
    venue = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    objects = models.Manager