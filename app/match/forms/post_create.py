from django import forms
from match.models.posts import Posts

class CreateForm(forms.Form):

    error_message = ''
    
    title = forms.CharField(label='TITLE', max_length=50,
    widget=forms.TextInput(
    attrs={'placeholder':'タイトルを入力して下さい', 'class':'form-control'}))
    
    number = forms.IntegerField(label='NUMBER',
    widget=forms.NumberInput(
    attrs={'placeholder':'募集人数を入力して下さい', 'class':'form-control'}))

    venue = forms.CharField(label='VENUE', max_length=30,
    widget=forms.TextInput(
    attrs={'placeholder':'開催地を入力して下さい', 'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, post):
        post = super().save()
        info = Posts()
        info.id = post.id
        info.title = post['title']
        info.number = post['number']
        info.venue = post['venue']
        
        info.save()

        self.is_save = True