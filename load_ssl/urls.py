from django.conf.urls import url
from load_ssl import views


urlpatterns = [
    url(
        r'^certificate/$',
        views.load_ssl,
        name='load_ssl'
    ),
    url(
        r'^sql/certificate/$',
        views.load_ssl_sql,
        name='load_ssl_sql'
    )
]
