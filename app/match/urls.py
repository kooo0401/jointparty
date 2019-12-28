from django.urls import path
from .views import index, user, post, reaction
from django.conf import settings
from django.conf.urls.static import static
from .controller import reaction_controller

app_name = 'match'

urlpatterns = [
    path('', index.top, name='index'),
    path('login/', index.Login.as_view(), name='login'),
    path('logout/', index.Logout.as_view(), name='logout'),
    path('users/', user.gets, name='users'),
    path('users/signup/', user.signup, name='signup'),
    path('users/profile/<int:user_id>', user.profile),
    path('users/<int:user_id>/edit/', user.edit),
    path('users/<int:userinfo_id>/create/', post.PostsCreateView.as_view(template_name='match/posts/create.html'), name='create'),
    path('posts_list/', post.PostListView.as_view(template_name='match/posts/posts_list.html'), name='posts_list'),
    path('reactions/', reaction_controller.create, name='reactions'),
    path('users/<int:user_id>/matching/', reaction.MatchListView.as_view(template_name='match/matching/match_list.html'), name='matching'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)