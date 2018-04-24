from django.db import models

# Create your models here.


class Station(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)
