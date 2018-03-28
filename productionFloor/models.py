from django.db import models

# Create your models here.
class Stations(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.id