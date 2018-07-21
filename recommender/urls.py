from django.conf.urls import url

from recommender import  views

urlpatterns = [
    url(r'^cf/user/(?P<user_id>\w+)/$',
        views.recs_cf, name='recs_cb'),
    url(r'^newsfeed/(?P<user_id>\w+)/(?P<longitude>\w+)/(?P<latitude>\w+)/(?P<page_number>\w+)/$',
        views.news_feed, name='news_feed'),
]