from django.db import models


class Orders(models.Model):
    products = models.TextField()
    #clientID = models.ForeignKey('Clients', on_delete=models.CASCADE())
    processes = models.TextField()

    def __str__(self):
        return self.id
