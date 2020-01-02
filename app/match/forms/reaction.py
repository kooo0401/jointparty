# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from match.models.reaction import Reaction

# class ReactionForm(forms.Form):

#     class Meta:
#       model = Reaction
#       fields = {
#           'status'
#       }


from django import forms
from match.models.posts import Posts
from match.models.reaction import Reaction

class ReactionForm(forms.Form):
    LIKE = 0
    reaction_users = Reaction()
    count = -1
    # image = Posts.objects.get(userinfo_id:)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self, user_id):
        mylikeusers = self.__toFromIdsArray(Reaction.objects.filter(from_user_id=user_id, status=self.LIKE))
        self.reaction_users = Reaction.objects.filter(to_post_id__in=mylikeusers, status=self.LIKE, from_user_id=user_id)
        self.count = len(self.reaction_users)
        # self.image = 


    def __toFromIdsArray(self, mylike_users):
        mylike_userids = list()
        for likeuser in mylike_users:
            mylike_userids.append(likeuser.to_post_id)
        return mylike_userids