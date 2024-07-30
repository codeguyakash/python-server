from rest_framework import viewsets
from contact.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from contact.api.permission import *
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class SolarInquiryViewSet(viewsets.ModelViewSet):
    queryset = SolarInquiry.objects.all()
    serializer_class = SolarInquirySerializer


class SolarStatusViewSet(viewsets.ModelViewSet):
    queryset = SolarStatus.objects.all()
    serializer_class = SolarStatusSerializer
    

    # def get_permissions(self):
        
    #     print("Current user:", self.request.user)
        
    #     print("Is channel partner:", self.request.user.is_channel_partner)
        
    #     if self.action in ['update', 'partial_update', 'destroy']:
    #         return [permissions.IsAuthenticated(), permissions.AllowAny()]
    #     # Temporarily allow any to test
    #     return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save() 




       



class SolarMaintanceViewSet(viewsets.ModelViewSet):
    queryset = SolarMaintanceInquries.objects.all()
    serializer_class = SolarMaintanceSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Ensures user is authenticated



class MaintanceStatusViewSet(viewsets.ModelViewSet):
    queryset = SolarMaintainceStatus.objects.all()
    serializer_class = SolarStatusMaintanceSerializer
    # permission_classes = [IsChannelPartner]

    def perform_create(self, serializer):
        solar_inquiry_id = self.request.data.get('solar_inquiry')
        if not solar_inquiry_id:
            raise ValidationError({"solar_inquiry": "This field is required."})

        if SolarMaintainceStatus.objects.filter(solar_inquiry_id=solar_inquiry_id).exists():
            raise ValidationError({"solar_inquiry": "A status record already exists for this inquiry."})

        serializer.save()
