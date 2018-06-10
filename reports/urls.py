from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.reports_index, name='index'),
    url(r'^coc/(?P<product_id>[0-9]+)$', views.coc, name='coc'),
    url(r'^delivery/(?P<order_id>[0-9]+)$', views.delivery, name='delivery'),
    url(r'^routing/(?P<product_id>[0-9]+)$', views.routing, name='routing'),
]
