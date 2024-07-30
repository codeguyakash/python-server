
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class WarrantyCardUpload(models.Model):
    solar_module_card    =models.FileField(upload_to='warranty_cards/')
    Inverter_module_card  =models.FileField(upload_to='Inverter_warranty_cards/')
    Battery_module_card  =models.FileField(upload_to='Battery_warranty_cards/')
    uploaded_by  =models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    upload_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uploaded_by}'s warranty card"
