from django.shortcuts import render, get_object_or_404

from .models import *
from .dictparser import *

def queryword(request):  
    query = request.GET.get('query')
    if query == None:
        word = None
    else:
        word = DictionaryWord(query)
    return render(request, 'queryword.html', {
        'word': word, 
    })
    