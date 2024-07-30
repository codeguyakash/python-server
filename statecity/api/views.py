from rest_framework import viewsets
from statecity.models import StateSubsidy
from .serializers import *

class StateSubsidyViewSet(viewsets.ModelViewSet):
    queryset = StateSubsidy.objects.all()
    serializer_class = StateSubsidySerializer
    



class CityViewset(viewsets.ModelViewSet):
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = City.objects.all()
        state_id = self.request.query_params.get('state_id', None)
        if state_id is not None:
            queryset = queryset.filter(statesubsidy__id=state_id)
        return queryset

    
    
