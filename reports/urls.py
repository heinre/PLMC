from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.reports_index, name='index'),
    url(r'^coc/(?P<product_id>[0-9]+)$', views.coc, name='coc'),
    url(r'^coc/delete/$', views.delete_coc, name='delete_coc'),
    url(r'^delivery/(?P<order_id>[0-9]+)$', views.delivery, name='delivery'),
    url(r'^potential/(?P<client_id>[0-9]+)$', views.potential, name='potential'),
    url(r'^routing/(?P<product_id>[0-9]+)$', views.routing, name='routing'),
    url(r'^routing/delete/$', views.delete_routing, name='delete_routing'),
]
