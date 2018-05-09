from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
import pulp
from production_floor.models import Product, Station
from . import forms
from django.http import JsonResponse
# Create your views here.


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


def _not_exist_page(request):
    return render(request, 'worker_info.html', {'nbar': 'workers',
                                                'worker': None})


def make_y_list():
    # get from DB the Queryset of products and of stations
    stations = Station.objects.all().values('type').distinct()  # todo might not be needed
    products = Product.objects.exclude(processes='')
    # make boolean array that indicates if process i should be on station j
    con_y_list = []
    con_t_list = []
    var_s_list = []
    for product in range(0, len(products)):
        temp = []
        temp2 = []
        temp3 = []
        for station in range(0, len(stations)):
            temp3.append(pulp.LpVariable('Sik: ' + str(product) + ',' + str(station), lowBound=0))
            if stations[station]['type'] in products[product].parse_machines():
                temp.append(1)
                temp2.append(1) #todo: change to knn
            else:
                temp.append(0)
                temp2.append(0)
        con_y_list.append(temp)
        con_t_list.append(temp2)
        var_s_list.append(temp3)
    return con_y_list, con_t_list, var_s_list, stations, products


def make_z_list(stations, products):
    con_z_list = []
    for product in range(0, len(products)):
        processes = products[product].parse_machines()
        temp = []
        for station_from in range(0, len(stations)):
            temp2 =[]
            for station_to in range(0, len(stations)):
                x = stations[station_from]
                y = stations[station_to]
                if "'"+str(x['type'])+"', '"+str(y['type'])+"'" in str(processes):
                    temp2.append(1)
                else:
                    temp2.append(0)
            temp.append(temp2)
        con_z_list.append(temp)
    return con_z_list


def make_x_list(stations, products):
    var_x_list = []
    for station in range(0, len(stations)):
        temp = []
        for product in range(0, len(products)):
            temp2 = []
            for next_product in range(0, len(products)):
                temp2.append(
                    pulp.LpVariable('Xijk: ' + str(product) + ',' + str(next_product) + ',' + str(station), lowBound=0, upBound=1,
                                    cat='Integer'))
            temp.append(temp2)
        var_x_list.append(temp)
    return var_x_list


def _build_lp():
    con_y_list, con_t_list, var_s_list, stations, products = make_y_list()
    con_z_list = make_z_list(stations, products)
    var_x_list = make_x_list(stations, products)
    M = pulp.LpVariable('M')
    lp = pulp.LpProblem("lp", pulp.LpMinimize)
    lp += M, 'M'


