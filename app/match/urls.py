from django.urls import path
from .views import index

app_name = 'match'

urlpatterns = [
    path('', index.top, name='index'),
]