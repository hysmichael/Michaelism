from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
    url(r'^$', 'dict.views.queryword', name='dict-queryword'),
)
