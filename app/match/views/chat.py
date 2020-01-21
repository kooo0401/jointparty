from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from match.controller import chat_controller
from match.forms.chat import ChatForm
import json


@login_required
def create(request, post_id):
    roomid = chat_controller.create(request.user.id, post_id)
    return redirect('/chat/show/' + str(roomid))

@login_required
def show(request, room_id):
    form = ChatForm(request.GET)
    form.load(request.user.id, room_id, request)
    context = {
        'form': form
    }
    template = loader.get_template('match/matching/chat.html')
    return HttpResponse(template.render(context, request))

@login_required
def messages(request, room_id):
    context = chat_controller.messages(room_id)
    context_json = json.dumps(context)
    return HttpResponse(context_json)