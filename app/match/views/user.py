from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from match.forms.user_signup import SignupForm
from match.forms.user_profile import ProfileForm
from match.forms.user_list import UserListForm
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from match.models.userinfo import UserInfo
from match.models.image import Image
from django.urls import reverse_lazy
from match.forms.user_edit import UserUpdateForm
from django.urls import reverse
from django import forms


def signup(request):
    if request.method == 'GET':
        form = SignupForm()
    else:
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            print('user_signup is_valid')
            form.save(request.POST)
            return redirect('/login/')
        else:
            print('user_signup false is_valid')

    template = loader.get_template('match/signup.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def gets(request):
    current_userid = request.user.id
    if request.method == 'GET':
        form = UserListForm(request.GET or None)
        form.load(current_userid)

    template = loader.get_template('match/users.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def profile(request, pk):
    if request.method == 'GET':
        form = ProfileForm(request.GET or None)
        form.load(pk)
        data = {
            'form': form,
            'iscurrent': request.user.id == pk,
        }
        return render(request, 'match/profile.html', data)

# カレントユーザー以外は404エラーを発生させる
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserUpdateView(OnlyYouMixin, LoginRequiredMixin, UpdateView):
    model = UserInfo
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def get_form(self):
        form = super(UserUpdateView, self).get_form()
        form.fields['name'].widget = forms.TextInput(attrs = {'class': 'form-control'})
        form.fields['name'].label = '名前'
        form.fields['self_introduction'].widget = forms.Textarea(attrs = {'class': 'form-control'})
        form.fields['self_introduction'].label = '自己紹介'
        # SEX = [('man','男'), ('woman','女')]
        # form.fields['sex'].choices = SEX
        # form.fields['sex'].widget = forms.RadioSelect()
        # form.fields['sex'].label = '性別'
        return form

    # 動的URLにリダイレクトする際は、下記メソッドを使う
    def get_success_url(self):
        return reverse_lazy('match:profile', kwargs={"pk":self.kwargs["pk"]})