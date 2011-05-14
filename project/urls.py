from django.conf.urls.defaults   import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib              import admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = \
    patterns('',
             (r'^admin/doc/',
              include('django.contrib.admindocs.urls')),
             
             (r'^admin/',
              include(admin.site.urls)),
             
             (r'^about/$',
              direct_to_template, { 'template' : 'about.html' }),

             (r'^$',
              direct_to_template, { 'template' : 'index.html' }),

             #(r'^.*$',
             # handler404),
             )
