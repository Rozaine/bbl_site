from django.db import models
from django.urls import reverse

class Ticket(models.Model):
    """Типичный класс модели, производный от класса Model."""
    ticket_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    tel_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20, blank=True)
    #time = models.DateTimeField(blank=True, default='')