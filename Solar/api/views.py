# from rest_framework import viewsets
# from Solar.models import SolarCalculator
# from .serializers import SolarCalculatorSerializer
# from rest_framework_simplejwt.authentication import JWTAuthentication


# class SolarCalculatorViewSet(viewsets.ModelViewSet):
#     queryset = SolarCalculator.objects.all()
#     serializer_class = SolarCalculatorSerializer
#     # authentication_classes=[JWTAuthentication]

from rest_framework import viewsets
from Solar.models import SolarCalculator
from .serializers import SolarCalculatorSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class SolarCalculatorViewSet(viewsets.ModelViewSet):
    queryset = SolarCalculator.objects.all()
    serializer_class = SolarCalculatorSerializer
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        # Proceed with the normal create operation
        return super().create(request, *args, **kwargs)


