from django.db import models

# Create your models here.
class addvehicle(models.Model):
    Sr=models.AutoField(primary_key=True)
    Regid=models.IntegerField(default=0)
    photo=models.ImageField(upload_to='addvehicle/')
    name=models.CharField(max_length=250, default="")
    route=models.CharField(max_length=300, default="")
    speed=models.CharField(max_length=200, default="")
    avgspeed=models.CharField(max_length=200, default="")
    engstatus=models.CharField(max_length=500, default="")
    fuel=models.IntegerField(default=0)
    temp=models.CharField(max_length=200, default="")
    staticmap=models.ImageField(upload_to='staticmap/')
    slug=models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name
    