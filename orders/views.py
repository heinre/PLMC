from django.shortcuts import render, redirect
from .models import Order
from clients.models import Client
from production_floor.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from . import forms


def orders_index(request):
    if request.GET:
        answer = Order.objects.filter(id__contains=request.GET['query']) | \
                 Order.objects.filter(clientID__name__contains=request.GET['query']) | \
                 Order.objects.filter(clientID__id__contains=request.GET['query'])
        print(answer)
        return render(request, 'order_page.html', {'nbar': 'orders', 'orders': answer,
                      'query': request.GET['query']})
    answer = Order.objects.filter(doneTime=None)
    return render(request, 'order_page.html', {'nbar': 'orders', 'orders': answer})


def _not_exist_page(request):
    return render(request, 'order_info.html', {'nbar': 'orders', 'order': None})


def orders_new(request):
    if request.method == 'POST':
        form = forms.OrderNew(request.POST)
        if form.is_valid():
            order = form.save()
            for i in range(0, int(request.POST['Pcounter'])):
                processes = request.POST['process'+str(i)]
                if processes[-1] == ',':
                    processes = processes[:-1]
                product = Product(name=request.POST['pname'+str(i)], order=order,
                                  amount=request.POST['pamount'+str(i)], processes=processes,
                                  parameters=request.POST['parameters'+str(i)])
                product.save()
            return redirect('orders:info', order.id)
        else:
            return render(request, 'order_new.html', {'nbar': 'orders', 'form': form})
    client = request.GET.get('client', '')
    if client:
        try:
            client = Client.objects.get(id=client)
            return render(request, 'order_new.html', {'nbar': 'orders', 'form': forms.OrderNew(), 'client': client})
        except ObjectDoesNotExist:
            return _not_exist_page(request)
    return render(request, 'order_new.html', {'nbar': 'orders', 'form': forms.OrderNew()})


def order_info(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        products = Product.objects.filter(order=order)
        return render(request, 'order_info.html', {'nbar': 'orders', 'order': order, 'products': products})
    except ObjectDoesNotExist:
        return _not_exist_page(request)


def order_edit(request, order_id):
    try:
        instance = Order.objects.get(id=order_id)
        if request.method == 'POST':
            form = forms.OrderNew(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                for i in range(0, int(request.POST['Pcounter'])):
                    product = Product(name=request.POST['pname' + str(i)], order=instance,
                                      amount=request.POST['pamount' + str(i)],
                                      processes=request.POST['process' + str(i)][:-1],
                                      parameters=request.POST['parameters'+str(i)])
                    product.save()
                return redirect('orders:info', order_id)
            else:
                return render(request, 'order_new.html', {'nbar': 'orders',
                                                           'form': forms.OrderNew(request.POST), 'edit': True})
        products = Product.objects.filter(order=instance)
        return render(request, 'order_new.html', {'nbar': 'orders',
                                                  'form': forms.OrderNew(instance=instance), 'products': products,
                                                  'edit': True})
    except ObjectDoesNotExist:
        return _not_exist_page(request)


def order_delete(request):
    if request.method == 'GET':
        return _not_exist_page(request)
    else:
        try:
            order = Order.objects.get(id=request.POST['id'])
            order.delete()
            print('deleted')
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'fail'})
