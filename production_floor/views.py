from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
#import pulp
from .models import Product
from . import forms
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


def _not_exist_page(request):
    return render(request, 'worker_info.html', {'nbar': 'workers',
                                                'worker': None})
"""
def _build_lp(proc,obj):
    #get from DB the list of products and parse that it we will have for each product the machines it should be on a.k Y_k

    var_y_list = [] #for each
    var_x_list = []
    var_s_list = []
    M = pulp.LpVariable('M')
    for k in range(0,proc):
        for i in range(0,obj):
            var_s_list.append(pulp.LpVariable('Sik: '+str(i)+','+str(k), lowBound=0))
            for j in range(0,obj):
                if i != j:
                    var_x_list.append(pulp.LpVariable('Xijk: '+str(i)+','+str(j)+','+str(k), lowBound=0, upBound=1, cat='Integer'))
    lp = pulp.LpProblem("lp", pulp.LpMinimize)
    lp += M ,'M'

"""

