from __future__ import unicode_literals

from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25)