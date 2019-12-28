from django.shortcuts import render, loader
from django.http import HttpResponse
from match.forms.reaction import ReactionForm
from django.views.generic import ListView
from match.models.reaction import Reaction

class MatchListView(ListView):
    model = Reaction
    form_class = ReactionForm

    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        context = super().get_context_data(**kwargs)
        
        return context