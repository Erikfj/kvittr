from django.conf.urls import patterns, url

from useraccounts import views

urlpatterns = patterns('',
    url(r'^$', views.user_listing, name='user_listing'),
    url(r'^(\d+)/$', views.user_details, name='user_details'),
    url(r'^(\d+)/increase_like$', views.user_increase_like, 
    	name='user_increase_like'),
)