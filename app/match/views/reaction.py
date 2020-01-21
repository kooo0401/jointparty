from django.shortcuts import render, loader
from django.http import HttpResponse
from match.forms.reaction import ReactionForm
from django.contrib.auth.decorators import login_required


@login_required
def matching(request, user_id):
    form = ReactionForm(request.GET)
    form.load(request.user.id)
    context = {
        'form': form,
    }
    # print(form.reaction_users[0].to_post.userinfo_id)
    template = loader.get_template('match/matching/match_list.html')
    return HttpResponse(template.render(context, request))