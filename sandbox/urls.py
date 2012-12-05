# The url routing methods we always need to include.
from django.conf.urls import patterns, include, url

# This allows us to send page request direct to template so we don't have to write
# the same type of view over and over again.
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sandbox.views.home', name='home'),
    # url(r'^sandbox/', include('sandbox.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),

    # (web) / -> (path) /base/templates/index.html
    url(r'^$', direct_to_template, {'template': 'base/index.html'}),

    # Skeleton responsive example.
    # (web) /skeleton/* -> (path) /skeleton/urls.py
    url(r'^skeleton/', include('skeleton.urls')),

    # Initializr responsive example.
    # (web) /initializr/* -> (path) /initializr/urls.py
    url(r'^initializr/', include('initializr.urls')),
)
