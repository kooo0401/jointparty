# クラスベースビューで記載

from django.shortcuts import render, loader, redirect
from match.forms.post_create import PostsCreateForm
from django.urls import reverse
from django.views.generic import ListView, CreateView
from match.models.posts import Posts
from django.urls import reverse_lazy


class PostsCreateView(CreateView):
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

class PostListView(ListView):
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