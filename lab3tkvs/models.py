from django.db import models

class Own(models.Model):
    name = models.CharField(max_length=120)
    tour = models.CharField(max_length=120)
    date = models.CharField(max_length=120)
    phone = models.IntegerField()
    address = models.CharField(max_length=1000)