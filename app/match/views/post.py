from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from match.forms.post_create import CreateForm

def create(request, user_id):
    # current_userid = request.user.id
    if request.method == 'GET':
        form = CreateForm()
    else:
        form = CreateForm(request.POST)
        if form.is_valid():
            print('post_create is_valid')
            form.save(request.POST)
            return redirect('/users/')
        else:
            print('post_create false is_valid')

    template = loader.get_template('match/posts/create.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def gets(request, user_id):
    return render(request, 'match/posts/posts.html')
    # current_userid = request.user.id
    if request.method == 'GET':
        form = CreateForm(requests.GET or None)
        form.load(user_id)
        data = {
            'form': form,
            'isurrent': request.use.id == user_id,
        }

    template = loader.get_template('match/posts/posts.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))