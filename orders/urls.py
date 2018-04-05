from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.orders_index, name='index'),
    url(r'^new/$', views.orders_new, name='new'),
    url(r'^(?P<order_id>[0-9]+)$', views.order_info, name='info'),
    url(r'^edit/(?P<order_id>[0-9]+)$', views.order_edit, name='edit'),
    url(r'^delete/$', views.order_delete),
]
