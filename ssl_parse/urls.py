from django.conf.urls import url, include

urlpatterns = [
    url(r'load/', include('load_ssl.urls', namespace='load_ssl')),
    url(r'edit/', include('edit_ssl.urls', namespace='edit_ssl')),
    url(r'delete/', include('delete_ssl.urls', namespace='delete_ssl')),
    url(r'^', include('view_ssl.urls', namespace='view_ssl')),
]
