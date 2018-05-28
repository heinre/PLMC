from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from production_floor.models import Product, Station
from . import forms
from django.http import JsonResponse
from django.utils import timezone
from operator import itemgetter
import json
import os



def product_edit(request, product_id):
    try:
        instance = Product.objects.get(id=product_id)
        if request.method == 'POST':
            form = forms.ProductForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('orders:edit', instance.order.id)
            else:
                print('something wrong')
                return render(request, 'product_edit.html', {'nbar': 'orders',
                                                           'form': forms.ProductForm(request.POST), 'edit': True})
        return render(request, 'product_edit.html', {'nbar': 'orders',
                                                   'form': forms.ProductForm(instance=instance), 'edit': True})
    except ObjectDoesNotExist:
        return _not_exist_page(request)


def product_delete(request):
    if request.method == 'GET':
        return _not_exist_page(request)
    else:
        try:
            product = Product.objects.get(id=request.POST['id'])
            product.delete()
            print('deleted')
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'fail'})


def station_new(request):
    if request.method == 'POST':
        form = forms.StationNew(request.POST)
        if form.is_valid():
            form.save()
            # create arbitrary knn information
            with open('./production_floor/utilities/times.json', 'r') as file:
                data = json.load(file)
            data[form.instance.type] = [[1, 2, 3, 1, 1, 120]]
            os.remove('./production_floor/utilities/times.json')
            with open('./production_floor/utilities/times.json', 'w') as file:
                file.write(json.dumps(data))
            # add empty list of scheduled products
            with open('./production_floor/utilities/schedule.json', 'r') as file:
                data = json.load(file)
            data[form.instance.type] = []
            os.remove('./production_floor/utilities/schedule.json')
            with open('./production_floor/utilities/schedule.json', 'w') as file:
                file.write(json.dumps(data))
            return redirect('production_floor:index')
        else:
            return render(request, 'station_new.html', {'nbar': 'production_floor', 'form': form})
    return render(request, 'station_new.html', {'nbar': 'production_floor', 'form': forms.StationNew()})


def station_edit(request, station_id):
    try:
        instance = Station.objects.get(id=station_id)
        if request.method == 'POST':
            form = forms.StationNew(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('production_floor:stations')
            else:
                return render(request, 'station_new.html', {'nbar': 'production_floor',
                                                           'form': forms.StationNew(request.POST), 'edit': True})
        pending_processes = Product.objects.filter(processes__contains=instance.type)
        return render(request, 'station_new.html', {'nbar': 'production_floor',
                                                    'form': forms.StationNew(instance=instance),
                                                    'edit': True, 'pending': len(pending_processes)})
    except ObjectDoesNotExist:
        return _not_exist_page(request)


def station_delete(request):
    if request.method == 'GET':
        return _not_exist_page(request)
    else:
        try:
            station = Station.objects.get(id=request.POST['id'])
            # deleting knn data
            with open('./production_floor/utilities/times.json', 'r') as file:
                data = json.load(file)
            del data[station.type]
            os.remove('./production_floor/utilities/times.json')
            with open('./production_floor/utilities/times.json', 'w') as file:
                file.write(json.dumps(data))
            # deleting from scheduling file
            with open('./production_floor/utilities/schedule.json', 'r') as file:
                data = json.load(file)
            del data[station.type]
            os.remove('./production_floor/utilities/schedule.json')
            with open('./production_floor/utilities/schedule.json', 'w') as file:
                file.write(json.dumps(data))
            station.delete()
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'fail'})


def show_stations(request):
    stations = Station.objects.all()
    return render(request, 'stations.html', {'nbar': 'production_floor', 'stations': stations})


def _not_exist_page(request):
    return render(request, 'station_info.html', {'nbar': 'workers',
                                                'station': None})


def schedule_index(request):
    with open('./production_floor/utilities/schedule.json') as file:
        schedule = json.load(file)
    schedule_dict = {}
    for station in Station.objects.all():
        schedule_dict[station.type] = []
        for product_tuple in schedule[station.type]:
            product = Product.objects.get(id=product_tuple[0])
            schedule_dict[station.type].append((product, product_tuple[3], product_tuple[4],
                                                timezone.now() + timezone.timedelta(seconds=product_tuple[4]-product_tuple[3]+60)))
    _list = []
    for key in schedule_dict:
        _list.append((key, schedule_dict[key], Station.objects.filter(type=key)[0].id))
    _list2 = []
    i = 0
    list_length = len(_list) if not len(_list) % 2 else len(_list)-1
    while i < list_length:
        _list2.append([_list.pop(0), _list.pop(0)])
        i += 2
    print(_list)
    print(_list2)
    return render(request, 'product_scheduling.html', {'nbar': 'production_floor', 'schedule': _list2,
                                                       'more': _list})


# machine, material, size, difficulty, oilled, packed, time
def order_products():
    answer = {}
    for station in Station.objects.all():
        answer[station.type] = []

    products = Product.objects.exclude(processes='')
    products_dict = {}
    for product in products:
        products_dict[product.id] = product.estimate_execution_time()
    while products_dict:
        next_to_schedule = {}
        for key in products_dict:
            temp = products_dict[key][0]
            if temp[2] in next_to_schedule:
                next_to_schedule[temp[2]].append((temp[0],temp[1],temp[3],temp[4],temp[5]))
            else:
                next_to_schedule[temp[2]] = [(temp[0], temp[1], temp[3],temp[4],temp[5])]
        for key in next_to_schedule:
            answer[key].append(sorted(next_to_schedule[key], key=itemgetter(4))[0])
            temp = answer[key][-1][-1]
            products_dict[answer[key][-1][0]].pop(0)
            if not products_dict[answer[key][-1][0]]:
                del products_dict[answer[key][-1][0]]
            else:
                _list = list(products_dict[answer[key][-1][0]][0])
                _list[4] = temp
                _list[5] = temp + _list[1] * _list[3]
                products_dict[answer[key][-1][0]][0] = tuple(_list)
        for key in products_dict:
            next_proc = products_dict[key][0]
            machine_finish = answer[next_proc[2]][-1][-1]
            if machine_finish > next_proc[-2]:
                temp = list(next_proc)
                temp[-2] = machine_finish
                temp[-1] = machine_finish + temp[1] * temp[3]
                products_dict[key][0] = tuple(temp)
    answer = json.dumps(answer)
    with open('./production_floor/utilities/schedule.json', 'w') as file:
        file.write(answer)


def schedule_view(request):
    order_products()
    return redirect('production_floor:index')
