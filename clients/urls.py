from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.clients_index, name='index'),
    url(r'^potential/$', views.potential_index, name='p_index'),
    url(r'^new/$', views.clients_new, name='new'),
    url(r'^potential/new/$', views.potential_new, name='p_new'),
    url(r'^(?P<client_id>[0-9]+)$', views.client_info, name='info'),
    url(r'^potential/(?P<client_id>[0-9]+)$', views.potential_info, name='p_info'),
    url(r'^edit/(?P<client_id>[0-9]+)$', views.client_edit, name='edit'),
    url(r'^potential/edit/(?P<client_id>[0-9]+)$', views.potential_edit, name='p_edit'),
    url(r'^delete/$', views.client_delete),
    url(r'^potential/delete/$', views.potential_delete),
]
