from rest_framework import serializers
from warrentycard.models import WarrantyCardUpload

class WarrantyCardUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarrantyCardUpload
        fields = ['solar_module_card', 'Inverter_module_card', 'Battery_module_card', 'uploaded_by', 'upload_date']
        read_only_fields = ['solar_module_card', 'Inverter_module_card', 'Battery_module_card', 'uploaded_by', 'upload_date']
