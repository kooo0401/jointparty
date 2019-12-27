from django.urls import path
from .views import index, user, post
from django.conf import settings
from django.conf.urls.static import static

app_name = 'match'

urlpatterns = [
    path('', index.top, name='index'),
    path('login/', index.Login.as_view(), name='login'),
    path('logout/', index.Logout.as_view(), name='logout'),
    path('users/', user.gets, name='users'),
    path('users/signup/', user.signup, name='signup'),
    path('users/profile/<int:user_id>', user.profile),
    path('users/<int:user_id>/edit/', user.edit),
    path('users/<int:user_id>/create/', post.CreateView.as_view(), name='create'),
    path('users/<int:user_id>/posts/', post.PostListView.as_view(), name='posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)