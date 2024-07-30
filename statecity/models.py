from django.db import models

# Create your models here.


class City(models.Model):
    city_name=models.CharField(max_length=100,null=True,default=None)
    
    
    def __str__(self):
        return self.city_name

class StateSubsidy(models.Model):
    state = models.CharField(max_length=100, unique=True)
    city=   models.ForeignKey(City,on_delete=models.CASCADE,default=None)
    subsidy_rate = models.FloatField(help_text="Subsidy rate as a percentage")
    state_generation = models.FloatField(help_text="Generation rate per state", default=None, null=True)



    def __str__(self):
       return self.state
   