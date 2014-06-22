from django.conf.urls import patterns, include, url, i18n
from django.shortcuts import render
from django.contrib import admin
from django.utils.translation import get_language
from intra import views

import activities.urls
import auth.urls
import forum.urls
import modules.urls
import tickets.urls
import users.urls

HOME_PAGE = 'intra/index.html'

admin.autodiscover()

urlpatterns = patterns('',
    # Home page
    url(r'^$', views.home, name="home"),
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
    # Modules
    url(r'^modules/', include(modules.urls, namespace='modules')),
    # Account management
    url(r'^activities/', include(activities.urls, namespace='activities')),
    # Internationalization
    url(r'^i18n/', include(i18n))
)
