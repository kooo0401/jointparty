from django.contrib import admin
from .models.userinfo import UserInfo
from .models.image import Image
from .models.posts import Posts
from .models.reaction import Reaction

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Image)
admin.site.register(Posts)
admin.site.register(Reaction)