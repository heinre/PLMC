from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.workers_index, name='index'),
    url(r'^new/$', views.workers_new, name='new'),
    url(r'^(?P<worker_id>[0-9]+)$', views.worker_info, name='info'),
    url(r'^edit/(?P<worker_id>[0-9]+)$', views.worker_edit, name='edit'),
    url(r'^delete/$', views.worker_delete),
    url(r'^shifts$', views.workers_shifts, name='shifts'),
]
