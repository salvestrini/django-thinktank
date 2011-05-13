from django.conf.urls.defaults   import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = \
    patterns('',
             #(r'^admin/doc/',
             # include('django.contrib.admindocs.urls')),
             
             #(r'^admin/',
             # include('admin.site.urls')),
             
             ('^about/$',
              direct_to_template, { 'template' : 'about.html' }),

             ('^$',
              direct_to_template, { 'template' : 'index.html' }),

             ('^.*$',
              handler404),
             )
