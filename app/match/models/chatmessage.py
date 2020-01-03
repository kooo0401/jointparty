from django.db import models
from match.models.chatroom import ChatRoom
from match.models.userinfo import UserInfo
from match.models.posts import Posts


class ChatMessage(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="message_roomid")
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="message_userid")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="message_postid")
    message = models.CharField(max_length=500)
    objects = models.Manager