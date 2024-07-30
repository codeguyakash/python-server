
from warrentycard.models import WarrantyCardUpload
from warrentycard.api.serializers import *
from rest_framework import viewsets, permissions
from contact.api.permission import *

class WarrantyCardUploadViewSet(viewsets.ModelViewSet):
    queryset = WarrantyCardUpload.objects.all()
    serializer_class = WarrantyCardUploadSerializer
    permission_classes = [permissions.IsAdminUser]  

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
