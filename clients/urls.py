from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.clients_index, name='index'),
    url(r'^new/$', views.clients_new, name='new'),
    url(r'^(?P<client_id>[0-9]+)$', views.client_info, name='info'),
    url(r'^edit/(?P<client_id>[0-9]+)$', views.client_edit, name='edit'),
    url(r'^delete/$', views.client_delete),
]
