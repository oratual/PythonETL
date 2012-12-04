# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Main.views',
    url(r'^create/$', 'create', name='list'),
)




#from django.conf.urls.defaults import patterns, url

#urlpatterns = patterns('myapp.views',
#    url(r'^list/$', 'list', name='list'),
#)