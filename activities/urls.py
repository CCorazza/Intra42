from django.conf.urls import patterns, url

from activities import views

urlpatterns = patterns('',
    url(r'^$', views.index_view, name='index'),
)
