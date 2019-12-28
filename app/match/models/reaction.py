from django.db import models
from match.models.userinfo import UserInfo
from match.models.posts import Posts

class Reaction(models.Model):
    to_post = models.ForeignKey(Posts, related_name="told", on_delete=models.CASCADE)
    from_user = models.ForeignKey(UserInfo, related_name="fromid", on_delete=models.CASCADE)
    status = models.IntegerField(primary_key=False)