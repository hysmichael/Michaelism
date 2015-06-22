from django.shortcuts import render, get_object_or_404

from .models import *
from .htmlengine import render_html_body, render_essay_introduction

def ideas_front_page(request):  
    essays = [{'object':e, 'intro':render_essay_introduction(e, 300)} for e in Essay.objects.order_by('-posted_at').all()]
    return render(request, 'ideas.html', {
        'active_nav': 'ideas', 
        'essays': essays,
    })
    
def ideas_single_essay(request, slug):
    essay = get_object_or_404(Essay, slug=slug)
    essay_body = render_html_body(essay)
    data  = {
                'active_nav':'ideas',
                'essay': essay,
                'essay_body': essay_body,
            }
    if essay.bundle is not None:
        related_essays = list(essay.bundle.essays.all())
        related_essays.remove(essay)
        data['related_essays'] = related_essays
    return render(request, 'essay.html', data)


