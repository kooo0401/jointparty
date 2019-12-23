from django import forms
from match.models.userinfo import UserInfo
from match.models.image import Image

class ProfileForm(forms.Form):
    info = UserInfo()
    image = Image()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self, userid):
        self.info = UserInfo.objects.get(pk=userid)
        self.image = Image.objects.get(pk=userid)