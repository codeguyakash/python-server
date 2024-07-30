from django.db import models
from statecity.models import City,StateSubsidy
from accounts.models import *
from accounts.models import *
from django.conf import settings
from contact.choice import *
from accounts.models import *



class SolarInquiry(models.Model):
    
    state=models.ForeignKey(StateSubsidy,on_delete=models.CASCADE,default=None) 
    city=models.ForeignKey(City,on_delete=models.CASCADE,default=None)
    interest_in = models.CharField(max_length=100, choices=INTEREST_CHOICES)
    name = models.CharField(max_length=255)
    contract_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255, blank=True, null=True)  
    email = models.EmailField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    address = models.TextField()
    comments = models.TextField(blank=True, null=True)
    distributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,default=None)


    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
    
        
     
class SolarStatus(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('incomplete', 'Incomplete'),
    ]

    solar_inquiry = models.OneToOneField(SolarInquiry, on_delete=models.CASCADE, related_name='status',primary_key=True)
    order_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    site_survey_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    installation_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    grid_connectivity_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Status for {self.solar_inquiry.name}"




class SolarMaintanceInquries(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='maintance_inquiries')
    state = models.ForeignKey(StateSubsidy, on_delete=models.CASCADE, related_name='maintance_inquiries',null=True)
    interest_in = models.CharField(max_length=100, choices=INTEREST_CHOICES)
    name = models.CharField(max_length=255)
    contract_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255, blank=True, null=True)  
    email = models.EmailField(max_length=255)
    pin_code = models.CharField(max_length=10)
    address = models.TextField()
    comments = models.TextField(null=True, blank=True)
    distributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)




class SolarMaintainceStatus(models.Model):

    solar_inquiry = models.OneToOneField(SolarMaintanceInquries, on_delete=models.CASCADE,default=None,primary_key=True)
    request_status = models.CharField(max_length=50, choices=REQUEST_CHOICE, default='Not Recieved')
    Technician_status = models.CharField(max_length=50, choices=TECHNICIAN_STATUS, default='pending')
    service_status = models.CharField(max_length=50, choices=SERVICE_STATUS, default='pending')
    request_status = models.CharField(max_length=50, choices=REQUEST_STATUS, default='pending')

    def __str__(self):
        return f"Status for {self.solar_inquiry.name}"

    


