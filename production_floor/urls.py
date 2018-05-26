from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^stations/$', views.show_stations, name='stations'),
    url(r'^stations/new/$', views.station_new, name='station_new'),
    url(r'^stations/edit/(?P<station_id>[0-9]+)$', views.station_edit, name='station_edit'),
    url(r'^stations/delete/$', views.station_delete),
    url(r'^products/edit/(?P<product_id>[0-9]+)$', views.product_edit, name='pedit'),
    url(r'^$', views.schedule_index, name='index'),
    url(r'^schedule/$', views.schedule_view, name='schedule'),
]
