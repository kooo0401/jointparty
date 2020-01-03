# クラスベースビューの成功版 views/post.py

class CreateView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': CreateForm(),
        }
        return render(request, 'match/posts/create.html', context)

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
create = CreateView.as_view()




# クラスベースビューの成功版 forms/post_create.py

from django import forms
from match.models.posts import Posts

class PostsCreateForm(forms.Form):

    error_message = ''
    
    title = forms.CharField(label='TITLE', max_length=50,
    widget=forms.TextInput(
    attrs={'placeholder':'例)  職業◯◯、平均年齢25歳です', 'class':'form-control'}))
    
    number = forms.IntegerField(label='NUMBER',
    widget=forms.NumberInput(
    attrs={'placeholder':'例)  4', 'class':'form-control'}))

    date = forms.DateField(label='DATE',
    widget=forms.DateInput(
    attrs={'placeholder':'例)  2019-12-25', 'class':'form-control'}))

    time = forms.TimeField(label='TIME',
    widget=forms.TimeInput(
    attrs={'placeholder':'例)  16:11:44', 'class':'form-control'}))

    venue = forms.CharField(label='VENUE', max_length=30,
    widget=forms.TextInput(
    attrs={'placeholder':'例)  渋谷', 'class':'form-control'}))

    is_save = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, post, user_id):
        info = Posts()
        info.title = post['title']
        info.number = post['number']
        info.date = post['date']
        info.time = post['time']
        info.venue = post['venue']
        info.userinfo_id = user_id
        
        info.save()

        self.is_save = True

# 投稿一覧の成功版 templates/posts/posts.html

{% load static %}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}

<meta name="viewport" content="width=device-width, initial-scale=1">

<div class="topPage">
    <div class="linkToLogin"><a href="/users/{{user.id}}/create">募集フォームを開く</a></div>
    {% for post in posts %}
        {{ post.title }}<br>
    {% endfor %}
</div>