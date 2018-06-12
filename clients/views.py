from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.messages import info
from django.http import JsonResponse
from . import forms
from .models import Client, PotentialClient
from orders.models import Order
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


def clients_index(request):
    clients_dict = {}
    if request.GET:
        answer = Client.objects.filter(name__contains=request.GET['query']) | \
                 Client.objects.filter(id__contains=request.GET['query']) | \
                 Client.objects.filter(address__contains=request.GET['query']) | \
                 Client.objects.filter(contactEmail__contains=request.GET['query']) | \
                 Client.objects.filter(contactName__contains=request.GET['query']) | \
                 Client.objects.filter(contactPhone__contains=request.GET['query'])
        for client in answer:
            clients_dict[client.id] = [client, len(Order.objects.filter(clientID=client)),
                                       len(Order.objects.filter(doneTime=None).filter(clientID=client))]
        return render(request, 'client_page.html', {'nbar': 'clients', 'clients': clients_dict,
                      'query': request.GET['query'], 'search': True})
    answer = Order.objects.filter(doneTime=None).order_by('clientID')
    for order in answer:
        client = order.clientID
        clients_dict[client.id] = [client, len(Order.objects.filter(clientID=client)),
                                   len(Order.objects.filter(doneTime=None).filter(clientID=client))]
    return render(request, 'client_page.html', {'nbar': 'clients', 'clients': clients_dict})


def _not_exist_page(request):
    return render(request, 'client_info.html', {'nbar': 'clients',
                                                'client': None})


def clients_new(request):
    if request.method == 'POST':
        form = forms.ClientNew(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('clients:info', client.id)
        else:
            return render(request, 'client_new.html', {'nbar': 'clients', 'form': form})
    return render(request, 'client_new.html', {'nbar': 'clients', 'form': forms.ClientNew()})


def potential_new(request):
    if request.method == 'POST':
        form = forms.PotentialNew(request.POST)
        if form.is_valid():
            form.instance.created = timezone.now()
            client = form.save()
            return redirect('clients:p_new', client.id)
        else:
            return render(request, 'potential_new.html', {'nbar': 'clients', 'form': form})
    return render(request, 'potential_new.html', {'nbar': 'clients', 'form': forms.PotentialNew()})


def client_info(request, client_id):
    try:
        client = Client.objects.get(id=client_id)
        done_orders = Order.objects.exclude(doneTime=None).filter(clientID__id=client_id)
        active_orders = Order.objects.filter(doneTime=None).filter(clientID__id=client_id)
        return render(request, 'client_info.html', {'nbar': 'clients',
                                                    'client': client, 'done_orders': done_orders,
                                                    'active_orders': active_orders})
    except ObjectDoesNotExist:
        return _not_exist_page(request)


def potential_info(request, client_id):
    try:
        client = PotentialClient.objects.get(id=client_id)
        return render(request, 'potential_info.html', {'nbar': 'clients', 'client': client})
    except ObjectDoesNotExist:
        return _not_exist_page(request)


def client_edit(request, client_id):
    try:
        instance = Client.objects.get(id=client_id)
        if request.method == 'POST':
            form = forms.ClientNew(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('clients:info', client_id)
            else:
                return render(request, 'client_new.html', {'nbar': 'clients',
                                                           'form': forms.ClientNew(request.POST), 'edit': True})
        return render(request, 'client_new.html', {'nbar': 'clients',
                                                   'form': forms.ClientNew(instance=instance), 'edit': True})
    except ObjectDoesNotExist:
        return _not_exist_page(request)


def client_delete(request):
    if request.method == 'GET':
        return _not_exist_page(request)
    else:
        try:
            client = Client.objects.get(id=request.POST['id'])
            client.delete()
            print('deleted')
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'fail'})



