from django.conf.urls import patterns, url

from modules import views

urlpatterns = patterns('',
    url(r'^$', views.list_modules, name='index'),
    url(r'^(?P<module>[^/]*)[/]?$', views.module_descr, name='module_descr'),
    url(r'^register/(?P<module>[^/]*)/(?P<user>[^/]*)[/]?$', views.module_register, name='module_register'),
)
