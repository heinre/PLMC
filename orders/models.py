from django.db import models
from django.utils.timesince import timesince, timeuntil
from django.utils import timezone


class Order(models.Model):
    products = models.TextField()
    clientID = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    processes = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    lastChanged = models.DateTimeField(auto_now=True, auto_now_add=False)
    dueDate = models.DateTimeField(null=True, blank=True)
    doneTime = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def late_due(self):
        if not self.doneTime:
            return timezone.now() > self.dueDate
        else:
            return self.doneTime > self.dueDate

    def get_process_time(self):
        if not self.doneTime:
            return '-'
        return timesince(self.created, self.doneTime)

    def get_duedone_difference(self):
        if self.doneTime > self.dueDate:
            return timesince(self.dueDate, self.doneTime)
        else:
            return timesince(self.doneTime, self.dueDate)

    def get_due_date(self):
        if not self.dueDate:
            return '-'
        return timeuntil(self.dueDate)

    def get_progress(self):
        if self.doneTime:
            return 100
        return 50         #write algorithm

    def get_cid(self):
        return self.clientID.id
