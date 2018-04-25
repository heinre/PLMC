from django.db import models
# Create your models here.


class Worker(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=400, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    availability = models.CharField(max_length=15,  default='ooooooooooooooo')
    skills = models.TextField()

    def __str__(self):
        return self.firstName + ' ' + self.lastName