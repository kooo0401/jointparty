# from django.shortcuts import render, loader
# from django.http import HttpResponse
# from match.forms.reaction import ReactionForm
# from django.views.generic import ListView
# from match.models.reaction import Reaction
# from match.models.posts import Posts
# from match.models.userinfo import UserInfo

# class MatchListView(ListView):
#     model = Reaction
#     # form_class = ReactionForm

#     def get_context_data(self, **kwargs):
#         LIKE = 0
#         reaction_users = Reaction()
#         count = -1
#         user_id = self.request.user.id
#         context = super().get_context_data(**kwargs)

#         mylike_userids = self.toFromIdsArray(Reaction.objects.filter(from_user_id=user_id, status=LIKE))
#         reaction_users = Reaction.objects.filter(to_post_id=mylike_userids, status=LIKE, from_user_id=user_id)
#         count = len(reaction_users)

#         return context

#     def toFromIdsArray(self, mylike_users):
#         mylike_userids = list()
#         for likeuser in mylike_userids:
#             mylike_userids.append(likeuser.to_post_id)
#         return mylike_userids


from django.shortcuts import render, loader
from django.http import HttpResponse
from match.forms.reaction import ReactionForm

def matching(request, user_id):
    form = ReactionForm(request.GET)
    form.load(request.user.id)
    context = {
        'form': form,
    }
    # print(form.reaction_users[0].to_post.userinfo_id)
    template = loader.get_template('match/matching/match_list.html')
    return HttpResponse(template.render(context, request))