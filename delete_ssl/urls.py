from django.conf.urls import url
from delete_ssl import views


urlpatterns = [
    url(
        r'^certificate/(?P<id>[\d]+)/$',
        views.delete_ssl,
        name='delete_ssl'
    ),
    url(
        r'^sql/certificate/(?P<id>[\d]+)/$',
        views.delete_ssl_sql,
        name='delete_ssl_sql'
    )
]
