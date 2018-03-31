from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.orders_index, name="index"),
]
