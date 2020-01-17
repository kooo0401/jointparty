from django import forms
from django.db import models
from match.models.userinfo import UserInfo


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('name', 'self_introduction',)
