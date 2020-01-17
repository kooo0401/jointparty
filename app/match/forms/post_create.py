from django import forms
from match.models.posts import Posts

class PostsCreateForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = (
            'title',
            'men_number',
            'women_number',
            'date',
            'time',
            'venue',
        )
        widgets = {
            "title": forms.TextInput(
            attrs={'placeholder':'例)  職業◯◯、平均年齢25歳です', 'class':'form-control'}),
            
            "men_number": forms.NumberInput(
            attrs={'placeholder':'例)  4', 'class':'form-control'}),

            "women_number": forms.NumberInput(
            attrs={'placeholder':'例)  4', 'class':'form-control'}),

            "date": forms.DateInput(
            attrs={'placeholder': '例)  2020-1-1', 'class': 'form-control'}),

            "time": forms.TimeInput(
            attrs={'placeholder': '例)  20:00', 'class': 'form-control'}),

            "venue": forms.TextInput(
            attrs={'placeholder':'例)  渋谷', 'class':'form-control'}),
        }