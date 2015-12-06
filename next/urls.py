from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
    url(r'^(?P<username>[a-z_]+)/$', 'next.views.next_view', name='next-page'),
    url(r'^(?P<username>[a-z_]+)/add/$', 'next.views.add_entry', name='add-entry'),
    url(r'^(?P<username>[a-z_]+)/modify/$', 'next.views.modify_entry', name='modify-entry'),
)
