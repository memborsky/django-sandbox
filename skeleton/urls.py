# The defaults.
from django.conf.urls import patterns, include, url

# Our django settings to be able to serve up static css/js/images.
from django.conf import settings

# Redirection
from django.views.generic.simple import redirect_to

# Craft our static routes.
import os

urlpatterns = patterns('',
    # our static stylesheets files
    url(r'^stylesheets/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': os.path.join(settings.OUR_ROOT, 'skeleton/static/stylesheets')
    }),

    # our static javascript files
    #url(r'^javascript/(?P<path>.*)$', 'django.views.static.serve', {
    #    'document_root': os.path.join(settings.OUR_ROOT, 'skeleton/static/javascript')
    #}),

    # our static images files
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': os.path.join(settings.OUR_ROOT, 'skeleton/static/images')
    }),

    # the root page
    url(r'^$', 'skeleton.views.index'),

    # redirect everything else back to /skeleton/
    url('[^ ]*', redirect_to, {'url': '/skeleton/'})
)
