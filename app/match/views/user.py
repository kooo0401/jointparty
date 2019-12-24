from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from match.forms.user_signup import SignupForm
from match.forms.user_profile import ProfileForm
from match.forms.user_edit import EditForm
from match.forms.user_list import UserListForm

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

def profile(request, user_id):
    if request.method == 'GET':
        form = ProfileForm(request.GET or None)
        form.load(user_id)
        data = {
            'form': form,
            'iscurrent': request.user.id == user_id,
        }
        return render(request, 'match/profile.html', data)

def edit(request, user_id):
    if request.method == 'GET':
        form = EditForm(request.GET or None)
        form.load(user_id)
    else:
        form = EditForm(request.POST or None, request.FILES)
        if form.is_valid():
            print('user_edit is_valid')
            form.save(request.POST, user_id)
        else:
            print('user_edit false is_valid')
        if form.is_save:
            return redirect('/users/profile/' + str(user_id))

    template = loader.get_template('match/edit.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))