from django.conf.urls import patterns, include, url, i18n
from django.shortcuts import render
from django.contrib import admin
from django.utils.translation import get_language

import auth.urls
import forum.urls
import tickets.urls
import users.urls

HOME_PAGE = 'intra/index.html'

admin.autodiscover()

urlpatterns = patterns('',
    # Home page
    url(r'^$', lambda request : render(request, HOME_PAGE), name='home'),
    # Admin panel
    url(r'^admin/', include(admin.site.urls)),
    # Account management
    url(r'^login/', include(auth.urls, namespace='auth')),
    # Forums
    url(r'^forum/', include(forum.urls, namespace='forum')),
    # Tickets
    url(r'^tickets/', include(tickets.urls, namespace='tickets')),
    # LDAP
    url(r'^users/', include(users.urls, namespace='users')),
    # Internationalization
    url(r'^i18n/', include(i18n))
)
