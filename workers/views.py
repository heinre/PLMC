from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .models import Worker
from production_floor.models import Station
import networkx as nx
from . import forms
import json
# Create your views here.


def workers_index(request):
    if not request.user.groups.filter(name='Manager').exists():
        return redirect('workers:shifts')
    if request.GET:
        answer = Worker.objects.filter(id__contains=request.GET['query']) | \
                 Worker.objects.filter(firstName__contains=request.GET['query']) | \
                 Worker.objects.filter(lastName__contains=request.GET['query']) | \
                 Worker.objects.filter(email__contains=request.GET['query']) | \
                 Worker.objects.filter(phone__contains=request.GET['query'])
        return render(request, 'worker_page.html', {'nbar': 'workers', 'workers': answer,
                      'query': request.GET['query']})
    answer = Worker.objects.all()
    return render(request, 'worker_page.html', {'nbar': 'workers', 'workers': answer})


def _not_exist_page(request):
    return render(request, 'worker_info.html', {'nbar': 'workers',
                                                'worker': None})


def workers_new(request):
    if request.method == 'POST':
        form = forms.WorkerNew(request.POST)
        if form.is_valid():
            worker = form.save()
            assign_shifts()
            return redirect('workers:info', worker.id)
        else:
            return render(request, 'worker_new.html', {'nbar': 'workers', 'form': form})
    return render(request, 'worker_new.html', {'nbar': 'workers', 'form': forms.WorkerNew()})


def worker_info(request, worker_id):
    try:
        worker = Worker.objects.get(id=worker_id)
        return render(request, 'worker_info.html', {'nbar': 'workers', 'worker': worker})
    except ObjectDoesNotExist:
        return _not_exist_page(request)


def worker_edit(request, worker_id):
    try:
        instance = Worker.objects.get(id=worker_id)
        if request.method == 'POST':
            form = forms.WorkerNew(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                assign_shifts()
                return redirect('workers:info', worker_id)
            else:
                return render(request, 'worker_new.html', {'nbar': 'workers',
                                                           'form': forms.WorkerNew(request.POST), 'edit': True})
        return render(request, 'worker_new.html', {'nbar': 'workers',
                                                   'form': forms.WorkerNew(instance=instance), 'edit': True})
    except ObjectDoesNotExist:
        return _not_exist_page(request)


def worker_delete(request):
    if request.method == 'GET':
        return _not_exist_page(request)
    else:
        try:
            worker = Worker.objects.get(id=request.POST['id'])
            worker.delete()
            print('deleted')
            assign_shifts()
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'fail'})


def workers_shifts(request):
    with open('./workers/utilities/shifts', 'r') as file:
        shifts = file.read()
    shifts = json.loads(shifts)
    named_shifts_dict = {}
    for key, value in shifts.items():
        for shift in value:
            if shift != 'x':
                value[value.index(shift)] = Station.objects.get(id=int(shift)).type
        named_shifts_dict[str(key) + ' - ' + str(Worker.objects.filter(pk=key)[0])] = value
    return render(request, 'worker_shifts.html', {'nbar': 'workers', 'shifts': named_shifts_dict})


def create_shifts_graph():
    graph = nx.DiGraph()
    graph.add_nodes_from(['B', 'T'])
    stations = Station.objects.all()
    # create nodes for each station at shift
    for station in stations:
        for shift in range(0, 15):
            graph.add_edge(('s', station.id, shift), 'T', capacity=1)
    # create worker
    for worker in Worker.objects.all():
        graph.add_edge('B', worker.id, capacity=5)
        # each worker have 5 days to work at
        for day in range(0, 5):
            graph.add_edge(worker.id, ('w', worker.id, day), capacity=1)
            # attach each station at shift to the worker's day
            for station in stations:
                if station.type in worker.skills.split(','):
                    for i in range(0, 3):
                        if worker.availability[day*3+i] == 'o':
                            graph.add_edge(('w', worker.id, day), ('s', station.id, day*3+i), capacity=1)
    return graph

def assign_shifts():
    graph = create_shifts_graph()
    flow_dict = nx.maximum_flow(graph, 'B', 'T')[1]
    print(flow_dict)
    shifts_dict = {}
    # initialize all workers to work none
    for worker in Worker.objects.all():
        shifts_dict[worker.id] = ['x'] * 15
    # check nodes that represent worker at a certain day
    for node in flow_dict:
        if type(node) is not int:
            if node[0] == 'w':
                for destination in flow_dict[node]:
                    # if there is flow for the i-th shift the i-th char in the string will be updated to the station id
                    if flow_dict[node][destination] > 0:
                        shifts_dict[node[1]][destination[2]] = str(destination[1])
    with open('./workers/utilities/shifts', 'w') as file:
        file.write(json.dumps(shifts_dict))


