from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.messages import info
from clients.models import Client
from production_floor.models import Station
import mimetypes
import json


def get_clients(request):
    if request.is_ajax():
        q = request.GET.get("term", '')
        clients = (Client.objects.filter(name__contains=q) | Client.objects.filter(id__contains=q))[:10]
        results = []
        for client in clients:
            client_json = {}
            client_json['label'] = '#' + str(client.id) + ' - ' + client.name
            client_json['value'] = client.id
            results.append(client_json)
        if not results:
            add_new = {}
            add_new['label'] = 'Add a new client'
            add_new['value'] = 0
            results.append(add_new)
        data = json.dumps(results)
        return HttpResponse(data)
    return redirect('homepage')


def get_stations(request):
    if request.is_ajax():
        stations = Station.objects.all().values('type').distinct()
        results = []
        for station in stations:
            results.append(station['type'])
        data = json.dumps(results)
        return HttpResponse(data)
    return redirect('homepage')


def index(request):
    return render(request, 'base.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homepage')
        else:
            info(request, 'Invalid Username/Password')
            if 'next' in request.POST:
                return redirect('/login/?next=%s' % request.POST.get('next'))
            return redirect('login')
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('homepage')
