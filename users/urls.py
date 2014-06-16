from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.users, name='users'),
	url(r'^profile/(?P<user>[^/]*)[/]?$', views.profile, name='profile'),
)