from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^products/edit/(?P<product_id>[0-9]+)$', views.product_edit, name='pedit'),
]
