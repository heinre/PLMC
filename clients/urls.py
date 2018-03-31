from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.clients_index, name='index'),
]
