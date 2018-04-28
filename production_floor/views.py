from django.shortcuts import render
#import pulp
#from .models import Product
# Create your views here.

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

