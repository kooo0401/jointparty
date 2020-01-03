from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from match.models.posts import Posts

class PostsCreateForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = (
            'title',
            'number',
            'date',
            'time',
            'venue',
        )
        widgets = {
            "title": forms.TextInput(
            attrs={'placeholder':'例)  職業◯◯、平均年齢25歳です', 'class':'form-control'}),
            
            "number": forms.NumberInput(
            attrs={'placeholder':'例)  4', 'class':'form-control'}),

            "date": forms.SelectDateWidget,

            "time": forms.TimeInput,

            "venue": forms.TextInput(
            attrs={'placeholder':'例)  渋谷', 'class':'form-control'}),
        }


    # error_message = ''
    
    # title = forms.CharField(label='TITLE', max_length=50,
    # widget=forms.TextInput(
    # attrs={'placeholder':'例)  職業◯◯、平均年齢25歳です', 'class':'form-control'}))
    
    # number = forms.IntegerField(label='NUMBER',
    # widget=forms.NumberInput(
    # attrs={'placeholder':'例)  4', 'class':'form-control'}))

    # date = forms.DateField(label='DATE',
    # widget=forms.DateInput(
    # attrs={'placeholder':'例)  2019-12-25', 'class':'form-control'}))

    # time = forms.TimeField(label='TIME',
    # widget=forms.TimeInput(
    # attrs={'placeholder':'例)  16:11:44', 'class':'form-control'}))

    # venue = forms.CharField(label='VENUE', max_length=30,
    # widget=forms.TextInput(
    # attrs={'placeholder':'例)  渋谷', 'class':'form-control'}))

    # is_save = False

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # def save(self, post, user_id):
    #     info = Posts()
    #     info.title = post['title']
    #     info.number = post['number']
    #     info.date = post['date']
    #     info.time = post['time']
    #     info.venue = post['venue']
    #     info.userinfo_id = user_id
        
    #     info.save()

    #     self.is_save = True