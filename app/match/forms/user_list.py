from django import forms
from match.models.userinfo import UserInfo

class UserListForm(forms.Form):
    exclude_userlist = UserInfo()
    list_length = -1
    currentuser_id = -1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self, user_id):
        self.currentuser_id = user_id
        # ログインユーザー以外のレコードを代入
        self.exclude_userlist = UserInfo.objects.exclude(pk=self.currentuser_id).order_by('-id')[:10]
        self.list_length = len(self.exclude_userlist)