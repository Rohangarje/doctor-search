from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    rating = models.FloatField()
    services = models.CharField(max_length=200, default='General Consultation')
    location = models.CharField(max_length=100, default='City Hospital')
    about = models.TextField(default='No information provided.')

    def __str__(self):
        return self.name