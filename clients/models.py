from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    contactName = models.CharField(max_length=100)
    contactEmail = models.EmailField(null=True, blank=True)
    contactPhone = models.CharField(max_length=15, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    #created = models.DateField.auto_now_add()
    #lastChanged = models.DateField.auto_now()
    #type = models.BooleanField() # new or interested

    def __str__(self):
        return self.name
