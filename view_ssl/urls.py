from django.conf.urls import url
from view_ssl import views


urlpatterns = [
    url(
        r'^$',
        views.all_ssl,
        name='all_ssl'
    ),
    url(
        r'^sql/$',
        views.all_ssl_sql,
        name='all_ssl_sql'
    ),
    url(
        r'^certificate/(?P<id>[\d]+)/$',
        views.one_ssl,
        name='one_ssl'
    ),
    url(
        r'^sql/certificate/(?P<id>[\d]+)/$',
        views.one_ssl_sql,
        name='one_ssl_sql'
    )
]
