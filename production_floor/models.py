from django.db import models

# Create your models here.

#todo: build a product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    amount = models.IntegerField()
    #executionTime = models.IntegerField() #list of execution times
    processes = models.TextField() #todo: add parameters of the product to estimate executionTime should consult Itzik

    # should return a list of machines and another list machines in order
    def parse_machines(self):
        pass

    # should initialize executionTime field
    def estimate_execution_time(self):
        pass

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Station(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)