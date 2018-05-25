from django.db import models
import json
from scipy.spatial import distance
from operator import itemgetter
# Create your models here.


def knn(data, point, k=5):
    num = k
    if k >= len(data):
        num = len(data)
    _list = []
    for element in data:
        _list.append((distance.euclidean(element[:-1], point), element[-1]))
    _list = sorted(_list, key=itemgetter(0))
    return _list[:num]


class Product(models.Model):
    name = models.CharField(max_length=200)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    amount = models.IntegerField()
    parameters = models.TextField(blank=True, null=True)
    done_processes = models.TextField(blank=True, null=True)
    coc = models.FileField(upload_to='media/coc', null=True, blank=True)
    processes = models.TextField(blank=True, null=True)

    # should return a list of machines and another list machines in order
    def parse_machines(self):
        processes_list = self.processes.split(',')
        return processes_list

    def parse_param(self):
        param_list = self.parameters.split(',')
        int_list = []
        for i in param_list:
            int_list.append(int(i))
        return int_list

    # should initialize executionTime field
    def estimate_execution_time(self):
        with open('./production_floor/utilities/times.json') as file:
            data = json.load(file)
        machines = self.parse_machines()
        estimation_list = []
        for machine in machines:
            machine_data = data[machine]
            param_list = self.parse_param()
            _list = knn(machine_data, param_list)
            avg = 0
            for element in _list:
                avg += element[1]
            avg = avg / len(_list)
            estimation_list.append((machine,avg))
        return estimation_list

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Station(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)