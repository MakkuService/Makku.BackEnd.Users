from django.db import models
from django.utils import timezone

#now = timezone.now()

class db_additional(models.Model):
    email = models.CharField(max_length=40, null=False)
    city = models.CharField(max_length=40, null=True, blank=True)
    coordinate = models.CharField(max_length=40, null=True, blank=True)
    IP = models.CharField(max_length=20, null=True, blank=True)
    lastpayment = models.CharField(max_length=20, null=True, blank=True)
    lastactivity = models.CharField(max_length=20, null=True, blank=True)
    createOn = models.CharField(max_length=20, null=True, blank=True)
    isactive = models.BooleanField(null=True, default=1)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.email} - {self.IP}'