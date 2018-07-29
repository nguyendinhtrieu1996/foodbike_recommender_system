from django.conf.urls import url

from recommender import  views

urlpatterns = [
    url(r'^cf/user/(?P<user_id>\w+)/$',
        views.recs_cf, name='recs_cb'),
    url(r'^newsfeed/(?P<user_id>[\w-]+)/(?P<longitude>\d+\.\d+)/(?P<latitude>\d+\.\d+)/(?P<page_number>\w+)/$',
        views.news_feed, name='news_feed'),
    url(r'^foods/$', views.get_all_foods, name='get_all_foods'),
]