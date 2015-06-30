from django.shortcuts import render, get_object_or_404

from .models import *
from .htmlengine import render_html_body

def ideas_front_page(request):  
    essays = Essay.objects.order_by('-posted_at').all()
    essays_by_year = {}
    current_year = None
    for essay in essays:
        if essay.posted_at.year == current_year:
            essays_by_year[current_year].append(essay)
        else:
            current_year = essay.posted_at.year
            essays_by_year[current_year] = [essay]

    return render(request, 'ideas.html', {
        'active_nav': 'ideas', 
        'essays_by_year': essays_by_year,
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


def projects_front_page(request):  
    return render(request, 'projects.html', {
        'active_nav': 'projects', 
    })

def visions_front_page(request):  
    return render(request, 'visions.html', {
        'active_nav': 'visions', 
    })


