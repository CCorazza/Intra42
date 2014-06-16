from django.conf.urls import patterns, url

from tickets import views

urlpatterns = patterns('',
    url(r'^$', views.index_view, name='index'),
    url(r'^ticket/(?P<pk>\d+)/', views.ticket_view, name='ticket'),
    url(r'^spool/', views.spool_view, name='spool'),
    # POSTs
    url(r'^new_ticket/', views.post_ticket, name='new_ticket'),
    url(r'^new_message/', views.post_message, name='new_message'),
    url(r'^assign_ticket/', views.post_assign, name='assign_ticket'),
    url(r'^change_status/', views.post_close, name='change_status'),
)
