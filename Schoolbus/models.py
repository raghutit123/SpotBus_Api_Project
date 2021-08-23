from django.db import models


# Create your models here.
class School(models.Model):
    School_id = models.IntegerField()
    School_name = models.CharField(max_length=100)
    School_address = models.CharField(max_length=200)
    School_location = models.CharField(max_length=100)

    def __str__(self):
        return self.School_id



class Route(models.Model):
    Route_id = models.IntegerField()
    School_id = models.IntegerField()
    Start_time = models.TimeField()
    Stop_CHOICES = [
        ('route_location','Route_location'),
        ('route_address','Route_address')]

    def __str__(self):
        return self.Route_id