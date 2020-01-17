# クラスベースビューで記載

from django.shortcuts import render, loader, redirect
from match.forms.post_create import PostsCreateForm
from django.urls import reverse
from django.views.generic import ListView, CreateView
from match.models.posts import Posts
from match.models.userinfo import UserInfo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PostsCreateView(CreateView, LoginRequiredMixin):
    model = Posts
    form_class = PostsCreateForm
    success_url = reverse_lazy('match:posts_list')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.userinfo_id = self.request.user.id

        return super(PostsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostListView(ListView, LoginRequiredMixin):
    model = Posts
    # ログインユーザー以外の投稿数を数値で取得(LisViewでデフォルトで返されるcontextの"object_list"を上書き)
    def get_queryset(self):
        current_user_id = self.request.user.id
        query_set = Posts.objects.exclude(userinfo_id=current_user_id).count()
        return query_set

    # ログインユーザー以外の投稿を全て取得
    def get_context_data(self, **kwargs):
        current_user_id = self.request.user.id
        context = super().get_context_data(**kwargs)
        context["posts_list"] = Posts.objects.exclude(userinfo_id=current_user_id).order_by('-id')
        return context

# "参加する"ボタン押下時の計算処理
def calculation(request, post_id):
    current_user = UserInfo.objects.get(pk=request.user.id)
    if current_user.sex == "man":
        add_post = Posts.objects.get(pk=post_id)
        add_post.men_restriction -= 1
        add_post.save()
    else:
        add_post = Posts.objects.get(pk=post_id)
        add_post.women_restriction -= 1
        add_post.save()
    
    return redirect('/users/' + str(current_user.id) +'/matching/')
