from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .models import Worker
from production_floor.models import Station
import networkx as nx
# Create your views here.


def workers_index(request):
    return render(request, 'worker_page.html', {'nbar': 'workers'})


def workers_shifts(request):
    workers_dict = {}
    for worker in Worker.objects.all():
        workers_dict[worker.id] = str(worker)
    return render(request, 'worker_page.html', {'nbar': 'workers', 'shifts': assign_shifts()})


def create_shifts_graph():
    graph = nx.Graph()
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
    shifts_dict = {}
    # initialize all workers to work none
    for worker in Worker.objects.all():
        shifts_dict[worker.id] = 'xxxxxxxxxxxxxxx'
    # check nodes that represent worker at a certain day
    for node in flow_dict:
        if type(node) is not int:
            if node[0] == 'w':
                for destination in flow_dict[node]:
                    # if there is flow for the i-th shift the i-th char in the string will be updated to the station id
                    if flow_dict[node][destination] > 0:
                        s = list(shifts_dict[node[1]])
                        s[destination[2]] = str(destination[1])
                        shifts_dict[node[1]] = ''.join(s)
    named_shifts_dict = {}
    for key, value in shifts_dict.items():
        named_shifts_dict[str(key) + ' - ' +str(Worker.objects.filter(pk=key)[0])] = value
    return named_shifts_dict
