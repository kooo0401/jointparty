from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from match.forms.login import LoginForm


def top(request):
    return render(request, 'match/index.html')

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'match/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'match/index.html'