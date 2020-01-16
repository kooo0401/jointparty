from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import (LogoutView)

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    username = forms.CharField(label='LOGIN_ID', max_length=30,
    widget=forms.TextInput(
    attrs={'placeholder':'名前を入力してください'}))

    password = forms.CharField(
    label='PASSWORD', max_length=128,
    widget=forms.PasswordInput(
    attrs={'placeholder':'パスワードを入力してください'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'match/login.html'