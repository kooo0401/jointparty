from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from match.forms.user_signup import SignupForm
from match.forms.user_profile import ProfileForm

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
    template = loader.get_template('users.html')
    context = {
        'form': '',
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