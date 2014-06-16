from django.conf.urls import patterns, url

from forum import views

urlpatterns = patterns('',
    url(r'^$', views.index_view, name='index'),
    url(r'^category/(?P<pk>\d+)/', views.category_view, name='category'),
    url(r'^thread/(?P<pk>\d+)/', views.thread_view, name='thread'),
    # POSTs
    url(r'^new_post/', views.post_reply, name='new_post'),
    url(r'^new_comment/', views.post_comment, name='new_comment'),
    url(r'^new_thread/', views.post_thread, name='new_thread'),
)
