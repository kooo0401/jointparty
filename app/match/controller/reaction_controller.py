from match.models.reaction import Reaction
from match.models.userinfo import UserInfo
from match.models.posts import Posts

def create(request):
    fromuser_id = request.user.id
    post = request.POST
    print(post)
    post_id = post["post_id"]
    reaction_status = post["reaction"]
    reactions = Reaction.objects.filter(to_post_id=post_id, from_user_id=fromuser_id)
    if(len(reactions) == 0):
        reaction = Reaction(to_post=Posts.objects.get(pk=post_id), from_user=UserInfo.objects.get(pk=fromuser_id), status=__status(reaction_status))
    else:
        reaction = reactions[0]
        reaction.status = __status(reaction_status)
    reaction.save()

def __status(status):
    if(status == "like"):
        return 0
    return 1