from django.db import models

class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    objects = models.Manager
    origin = models.ImageField(upload_to="photos/%y/%m/%d/")