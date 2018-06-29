from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^stations/$', views.show_stations, name='stations'),
    url(r'^stations/new/$', views.station_new, name='station_new'),
    url(r'^stations/edit/(?P<station_id>[0-9]+)$', views.station_edit, name='station_edit'),
    url(r'^stations/delete/$', views.station_delete),
    url(r'^$', views.schedule_index, name='index'),
    url(r'^schedule/$', views.schedule_view, name='schedule'),
    url(r'^wip/$', views.wip_view, name='wip'),
    url(r'^start/$', views.start_process, name='start'),
    url(r'^end/$', views.end_process, name='end'),
]
