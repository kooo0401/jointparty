from django.shortcuts import render, loader
from django.http import HttpResponse
from match.forms.reaction import ReactionForm
from django.views.generic import ListView

def MatchListView(ReactionForm):
    