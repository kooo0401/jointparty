from django.urls import path
from .views import index, user

app_name = 'match'

urlpatterns = [
    path('', index.top, name='index'),
    path('users/signup/', user.signup, name='signup'),
]