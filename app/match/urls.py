from django.urls import path
from .views import index, user, post, reaction, chat
from django.conf import settings
from django.conf.urls.static import static
from .controller import reaction_controller, chat_controller
# ①ログインユーザーはログインページに入れないように
from django.contrib.auth.views import LoginView


app_name = 'match'

urlpatterns = [
    path('', index.top, name='index'),
    # ②ログインユーザーはログインページに入れないように
    path('login/', index.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', index.Logout.as_view(), name='logout'),
    path('users/', user.gets, name='users'),
    path('users/signup/', user.signup, name='signup'),
    path('users/profile/<int:pk>', user.profile, name="profile"),
    path('users/<int:pk>/edit/', user.UserUpdateView.as_view(template_name='match/edit.html'), name="update"),
    path('users/<int:userinfo_id>/create/', post.PostsCreateView.as_view(template_name='match/posts/create.html'), name='create'),
    path('posts_list/', post.PostListView.as_view(template_name='match/posts/posts_list.html'), name='posts_list'),
    path('reactions/', reaction_controller.create, name='reactions'),
    # path('users/<int:user_id>/matching/', reaction.MatchListView.as_view(template_name='match/matching/match_list.html'), name='matching'),
    path('users/<int:user_id>/matching/', reaction.matching, name='matching'),
    path('chat/create/<int:post_id>', chat.create, name='chat_create'),
    path('chat/show/<int:room_id>', chat.show, name='chat_show'),
    path('chat/show/<int:room_id>/messages/', chat.messages, name='chat_messages'),
    path('posts/calculation/<int:post_id>', post.calculation),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)