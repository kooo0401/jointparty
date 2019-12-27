# クラスベースビューで記載

from django.shortcuts import render, loader, redirect
from match.forms.post_create import CreateForm
from django.urls import reverse
from django.views.generic import TemplateView
from match.models.posts import Posts


class CreateView(TemplateView):
    template_name = 'match/posts/create.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, user_id, *args, **kwargs):
        form = CreateForm(request.POST)
        if form.is_valid():
            print("検証に成功しました。データを保存します")
            form.save(request.POST, user_id)
            return redirect('/users/')
        else:
            print("検証に失敗したので、データを保存しません。検証に失敗した理由を次に表示します。")
            print(form.errors)
        # return redirect(reverse('match:create', user_id))
        return redirect('/users/'+ str(user_id)+'/create/')

class PostListView(TemplateView):
    def get(self, request, user_id, *args, **kwargs):
        posts = Posts.objects.all().order_by('-id')

        return render(request, 'match/posts/posts.html', {'posts': posts})



    #     class CreateView(TemplateView):
    # template_name = 'match/posts/create.html'
    # def get(self, request, *args, **kwargs):
    #     context = {
    #         'form': CreateForm(),
    #     }
    #     return context

    # def post(self, request, user_id, *args, **kwargs):
    #     form = CreateForm(request.POST)
    #     if form.is_valid():
    #         print("検証に成功しました。データを保存します")
    #         form.save(request.POST, user_id)
    #         return redirect('/users/')
    #     else:
    #         print("検証に失敗したので、データを保存しません。検証に失敗した理由を次に表示します。")
    #         print(form.errors)
    #     # return redirect(reverse('match:create', user_id))
    #     return redirect('/users/'+ str(user_id)+'/create/')
