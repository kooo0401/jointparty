# from django import forms
# from match.models.posts import Posts

# class PostListForm(forms.Form):
#     exclude_userlist = Posts()
#     list_length = -1
#     currentuser_id = -1

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def get(self, user_id):
#         self.currentuser_id = user_id
#         # ログインユーザー以外のレコードを代入
#         self.exclude_userlist = Posts.objects.exclude(userinfo_id=self.currentuser_id)
#         self.list_length = len(self.exclude_userlist)

# from django import forms
# from match.models.posts import Posts

# class PostListForm(forms.Form):
#     exclude_userlist = Posts()
#     list_length = -1
#     currentuser_id = -1

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def load(self, user_id):
#         self.currentuser_id = user_id
#         # ログインユーザー以外のレコードを代入
#         self.exclude_userlist = Posts.objects.exclude(userinfo_id=self.currentuser_id)
#         self.list_length = len(self.exclude_userlist)