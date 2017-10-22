from django.conf.urls import url
from edit_ssl import views


urlpatterns = [
    url(
        r'^certificate/(?P<id>[\d]+)/$',
        views.edit_ssl,
        name='edit_ssl'
    ),
    url(
        r'^sql/certificate/(?P<id>[\d]+)/$',
        views.edit_ssl_sql,
        name='edit_ssl_sql'
    )
]
