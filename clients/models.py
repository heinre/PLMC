from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    contactName = models.CharField(max_length=100)
    contactEmail = models.EmailField(null=True, blank=True)
    contactPhone = models.CharField(max_length=15, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class PotentialClient(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    contactName = models.CharField(max_length=100)
    contactEmail = models.EmailField(null=True, blank=True)
    contactPhone = models.CharField(max_length=15, null=True, blank=True)
    field = models.CharField(max_length=400)
    operator = models.CharField(max_length=100)
    rf_choices = (
        ('GL', 'Google'),
        ('WS', 'ביקור באתר'),
        ('NP', 'עיתון'),
        ('RC', 'המלצה'),
        ('OT', 'אחר'),
    )
    referred = models.CharField(
        max_length=2,
        choices=rf_choices,
        default='OT'
    )
    remarks = models.TextField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
