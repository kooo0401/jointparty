from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from match.forms.user_signup import SignupForm

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