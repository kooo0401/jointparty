from django import forms
from django.contrib.auth.forms import AuthenticationForm
from match.models.reaction import Reaction

class ReactionForm(forms.Form):

    class Meta:
      model = Reaction
      fields = {
          'status'
      }