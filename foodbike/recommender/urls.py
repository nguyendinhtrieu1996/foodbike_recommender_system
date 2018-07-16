from django.conf.urls import url

from recommender import  views

urlpatterns = [
    url(r'^cf/user/(?P<user_id>\w+)/$',
        views.recs_cf, name='recs_cb'),
    url(r'^cf/sql/', views.excute_sql, name='excute_sql'),
]