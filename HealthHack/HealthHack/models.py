from django.db import models

# Create your models here.

# company Profile
class company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    currentPopulation = models.IntegerField()

class dailyAverage(models.Model):
    companyID = models.ForeignKey('Company', on_delete=models.CASCADE)
    time = models.TimeField()
    population = models.IntegerField()
    count = models.IntegerField()

class log(models.Model):
    companyId = models.ForeignKey('Company', on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add = True)
    population = models.IntegerField()
    date = models.DateField()
