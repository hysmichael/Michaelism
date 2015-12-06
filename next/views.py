from django.shortcuts import render
from django.http import HttpResponse

import json

from models import *

def next_view(request, username):
    try:
        NextUser.objects.get(username=username)
        entries_I   = NextEntry.objects.filter(username=username, done=False, list_id=1).order_by('created_at').all()
        entries_II  = NextEntry.objects.filter(username=username, done=False, list_id=2).order_by('created_at').all()
        return render(request, 'next.html', {
            'username': username,
            'list_I': entries_I,
            'list_II': entries_II,
        })
    except NextUser.DoesNotExist:
        return render(request, 'next_unauthorized.html')

def add_entry(request, username):
    json_data = json.loads(request.body)
    content = json_data['content']
    list_id = json_data['list_id']
    new_entry = NextEntry(content=content, username=username, list_id=list_id)
    new_entry.save()
    return HttpResponse('Created.', status=201)

def modify_entry(request, username):
    json_data = json.loads(request.body)
    entry_id = json_data['entry_id']
    status = (json_data['status'] == 'true')
    entry = NextEntry.objects.get(pk=entry_id)
    if entry.username != username:
        return HttpResponse('Invalid Entry ID.', status=400)
    entry.done = status
    entry.save()
    return HttpResponse('Modified.', status=200)

