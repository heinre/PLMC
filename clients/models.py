from django.db import models

# Create your models here.
class Clients(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    type = models.BooleanField() # new or interested

    def __str__(self):
        return self.firstName + self.lastName