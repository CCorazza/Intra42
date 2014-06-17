from django.conf.urls import patterns, url

from modules import views

urlpatterns = patterns('',
    url(r'^$', views.index_view, name='index'),
    #url(r'^(?P<cat>[^/]*)[/]?$', views.modules_view, name='modules'),
)
