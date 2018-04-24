from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.workers_index, name='index'),
    url(r'^shifts$', views.workers_shifts, name='shifts'),
]
