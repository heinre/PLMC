from django.conf.urls import url
from . import views
from production_floor import views as p_views

urlpatterns = [
    url(r'^$', views.orders_index, name='index'),
    url(r'^new/$', views.orders_new, name='new'),
    url(r'^(?P<order_id>[0-9]+)$', views.order_info, name='info'),
    url(r'^edit/(?P<order_id>[0-9]+)$', views.order_edit, name='edit'),
    url(r'^product/edit/(?P<product_id>[0-9]+)$', p_views.product_edit, name='pedit'),
    url(r'^product/delete/$', p_views.product_delete, name='pdelete'),
    url(r'^product/parameters/(?P<product_id>[0-9]+)$', p_views.product_parameters, name='pparameters'),
    url(r'^delete/$', views.order_delete),
]
