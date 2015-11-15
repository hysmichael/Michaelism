from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import *

urlpatterns = patterns('',
    url(r'^$', 'pages.views.index_page', name='home-page'),
    # url(r'^ideas/$', 'pages.views.ideas_front_page', name='ideas-front-page'),
    url(r'^ideas/(?P<slug>[^\.]+)/$', 'pages.views.ideas_single_essay', name='ideas-single-essay'),
)
