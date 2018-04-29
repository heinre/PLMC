"""PLMC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from PLMC import views


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^clients/', include('clients.urls', namespace='clients')),
    url(r'^reports/', include('reports.urls', namespace='reports')),
    url(r'^workers/', include('workers.urls', namespace='workers')),
    url(r'^productionFloor/', include('production_floor.urls', namespace='production_floor')),
    url(r'^api/clients/', views.get_clients),
    url(r'^api/stations/', views.get_stations),
]
